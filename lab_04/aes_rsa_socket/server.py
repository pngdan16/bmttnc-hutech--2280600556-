from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import socket
import threading
import hashlib

# Initialize server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)

# Generate RSA key pair
server_key = RSA.generate(2048)

# List of connected clients
clients = []

# Function to encrypt message
def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + ciphertext

# Function to decrypt message
def decrypt_message(key, encrypted_message):
    iv = encrypted_message[:AES.block_size]
    ciphertext = encrypted_message[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_message.decode()

# Function to handle client connection
def handle_client(client_socket, client_address):
    aes_key = None  # Initialize aes_key to None at the start
    try:
        print(f"Connected with {client_address}")

        # Send server's public key to client
        public_key_pem = server_key.publickey().export_key(format='PEM')
        client_socket.send(public_key_pem)

        # Receive client's public key
        client_key_pem = client_socket.recv(4096)  # Increased buffer size
        try:
            client_received_key = RSA.import_key(client_key_pem)
        except ValueError as e:
            print(f"Error importing client key: {e}")
            print(f"Received key data: {client_key_pem.hex()}")  # Print as hex for better debugging
            return

        # Generate AES key for message encryption
        aes_key = get_random_bytes(16)
        
        # Encrypt the AES key using the client's public key
        cipher_rsa = PKCS1_OAEP.new(client_received_key)
        encrypted_aes_key = cipher_rsa.encrypt(aes_key)
        client_socket.send(encrypted_aes_key)

        # Add client to the list
        clients.append((client_socket, aes_key))

        while True:
            try:
                encrypted_message = client_socket.recv(1024)
                if not encrypted_message:  # Client disconnected
                    break
                    
                decrypted_message = decrypt_message(aes_key, encrypted_message)
                print(f"Received from {client_address}: {decrypted_message}")

                # Send received message to all other clients
                for client, client_aes_key in clients:
                    if client != client_socket:
                        try:
                            encrypted = encrypt_message(client_aes_key, decrypted_message)
                            client.send(encrypted)
                        except Exception as e:
                            print(f"Error sending to client: {e}")

                if decrypted_message == "exit":
                    break

            except Exception as e:
                print(f"Error processing message from {client_address}: {e}")
                break

    except Exception as e:
        print(f"Error handling client {client_address}: {e}")
    
    finally:
        # Clean up when client disconnects
        if aes_key is not None and (client_socket, aes_key) in clients:
            clients.remove((client_socket, aes_key))
        try:
            client_socket.close()
        except:
            pass
        print(f"Connection with {client_address} closed")

# Accept and handle client connections
print("Server started, waiting for connections...")
while True:
    try:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()
    except Exception as e:
        print(f"Error accepting connection: {e}")
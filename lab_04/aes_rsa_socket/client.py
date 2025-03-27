from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import socket
import threading

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

def receive_messages(client_socket, aes_key):
    while True:
        try:
            encrypted_message = client_socket.recv(1024)
            if not encrypted_message:
                break
            decrypted_message = decrypt_message(aes_key, encrypted_message)
            print(f"\nReceived: {decrypted_message}")
        except Exception as e:
            print(f"Error receiving message: {e}")
            break
    client_socket.close()

def handle_server_connection():
    try:
        # Create client socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 12345))

        # Generate client's RSA key pair
        client_key = RSA.generate(2048)
        
        # Receive server's public key
        server_key_pem = client_socket.recv(4096)
        server_public_key = RSA.import_key(server_key_pem)

        # Send client's public key to server
        client_socket.send(client_key.publickey().export_key(format='PEM'))

        # Receive encrypted AES key from server
        encrypted_aes_key = client_socket.recv(512)
        cipher_rsa = PKCS1_OAEP.new(client_key)
        aes_key = cipher_rsa.decrypt(encrypted_aes_key)

        # Start receiving messages in a separate thread
        receive_thread = threading.Thread(target=receive_messages, args=(client_socket, aes_key))
        receive_thread.daemon = True
        receive_thread.start()

        # Main loop for sending messages
        print("Connected to server. Type 'exit' to quit.")
        while True:
            message = input("Enter message: ")
            encrypted_message = encrypt_message(aes_key, message)
            client_socket.send(encrypted_message)
            if message.lower() == "exit":
                break

    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    handle_server_connection()

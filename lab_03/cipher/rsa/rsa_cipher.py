import rsa
import os

class RSACipher:
    def __init__(self):
        self.public_key = None
        self.private_key = None
        # Đường dẫn đến thư mục keys trong module rsa
        self.keys_dir = os.path.join(os.path.dirname(__file__), 'keys')

    def generate_keys(self):
        try:
            # Tạo cặp khóa mới
            (self.public_key, self.private_key) = rsa.newkeys(2048)
            
            # Đảm bảo thư mục keys tồn tại
            if not os.path.exists(self.keys_dir):
                os.makedirs(self.keys_dir)
            
            # Lưu public key
            public_key_path = os.path.join(self.keys_dir, 'public.pem')
            with open(public_key_path, 'wb') as f:
                f.write(self.public_key.save_pkcs1('PEM'))
            
            # Lưu private key
            private_key_path = os.path.join(self.keys_dir, 'private.pem')
            with open(private_key_path, 'wb') as f:
                f.write(self.private_key.save_pkcs1('PEM'))
            
            return True
        except Exception as e:
            print(f"Error generating keys: {str(e)}")
            return False

    def load_keys(self):
        try:
            # Đọc public key
            public_key_path = os.path.join(self.keys_dir, 'public.pem')
            with open(public_key_path, 'rb') as f:
                self.public_key = rsa.PublicKey.load_pkcs1(f.read())
            
            # Đọc private key
            private_key_path = os.path.join(self.keys_dir, 'private.pem')
            with open(private_key_path, 'rb') as f:
                self.private_key = rsa.PrivateKey.load_pkcs1(f.read())
            
            return self.private_key, self.public_key
        except FileNotFoundError:
            print("Keys not found in cipher/rsa/keys. Please generate keys first.")
            return None, None
        except Exception as e:
            print(f"Error loading keys: {str(e)}")
            return None, None

    def encrypt(self, message, key):
        try:
            return rsa.encrypt(message.encode(), key)
        except Exception as e:
            print(f"Error encrypting: {str(e)}")
            return None

    def decrypt(self, ciphertext, key):
        try:
            return rsa.decrypt(ciphertext, key).decode()
        except Exception as e:
            print(f"Error decrypting: {str(e)}")
            return None

    def sign(self, message, private_key):
        try:
            return rsa.sign(message.encode(), private_key, 'SHA-256')
        except Exception as e:
            print(f"Error signing: {str(e)}")
            return None

    def verify(self, message, signature, public_key):
        try:
            rsa.verify(message.encode(), signature, public_key)
            return True
        except rsa.VerificationError:
            return False
        except Exception as e:
            print(f"Error verifying: {str(e)}")
            return False
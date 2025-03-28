from flask import Flask, request, jsonify
from cipher.rsa import RSACipher
from cipher.ecc import ECCCipher
app = Flask(__name__)
# RSA CIPHER ALGORITHM
rsa_cipher = RSACipher()
# ECC CIPHER ALGORITHM
ecc_cipher = ECCCipher()

# @app.route('/api/rsa/generate_keys', methods=['GET'])
# def generate_keys():
#     if rsa_cipher.generate_keys():
#         return jsonify({"message": "Keys generated successfully"})
#     return jsonify({"error": "Failed to generate keys"}), 500

# @app.route('/api/rsa/encrypt', methods=['POST'])
# def rsa_encrypt():
#     data = request.json
#     message = data['message']
#     key_type = data['key_type']
    
#     private_key, public_key = rsa_cipher.load_keys()
#     if not private_key or not public_key:
#         return jsonify({'error': 'Keys not found'}), 500

#     if key_type == 'public':
#         key = public_key
#     elif key_type == 'private':
#         key = private_key
#     else:
#         return jsonify({'error': 'Invalid key type'}), 400

#     encrypted_message = rsa_cipher.encrypt(message, key)
#     if encrypted_message is None:
#         return jsonify({'error': 'Encryption failed'}), 500
        
#     encrypted_hex = encrypted_message.hex()
#     return jsonify({'encrypted_message': encrypted_hex})

# @app.route("/api/rsa/decrypt", methods=['POST'])
# def rsa_decrypt():
#     data = request.json
#     ciphertext_hex = data['cipher_text']
#     key_type = data['key_type']
    
#     private_key, public_key = rsa_cipher.load_keys()
#     if not private_key or not public_key:
#         return jsonify({'error': 'Keys not found'}), 500

#     if key_type == 'public':
#         key = public_key
#     elif key_type == 'private':
#         key = private_key
#     else:
#         return jsonify({'error': 'Invalid key type'}), 400
    
#     try:
#         ciphertext = bytes.fromhex(ciphertext_hex)
#     except ValueError:
#         return jsonify({'error': 'Invalid hex string'}), 400

#     decrypted_message = rsa_cipher.decrypt(ciphertext, key)
#     if decrypted_message is None:
#         return jsonify({'error': 'Decryption failed'}), 500

#     return jsonify({'decrypted_message': decrypted_message})

# @app.route('/api/rsa/sign', methods=['POST'])
# def rsa_sign():
#     data = request.json
#     message = data['message']
    
#     private_key, _ = rsa_cipher.load_keys()
#     if not private_key:
#         return jsonify({'error': 'Private key not found'}), 500

#     signature = rsa_cipher.sign(message, private_key)
#     if signature is None:
#         return jsonify({'error': 'Signing failed'}), 500
        
#     signature_hex = signature.hex()
#     return jsonify({'signature': signature_hex})

# @app.route('/api/rsa/verify', methods=['POST'])
# def rsa_verify():
#     data = request.json
#     message = data['message']
#     signature_hex = data['signature']
    
#     _, public_key = rsa_cipher.load_keys()
#     if not public_key:
#         return jsonify({'error': 'Public key not found'}), 500

#     try:
#         signature = bytes.fromhex(signature_hex)
#     except ValueError:
#         return jsonify({'error': 'Invalid signature hex string'}), 400

#     is_verified = rsa_cipher.verify(message, signature, public_key)
#     return jsonify({'is_verified': is_verified})

@app.route('/api/ecc/generate_keys', methods=['GET'])
def generate_keys():
    ecc_cipher.generate_keys()
    return jsonify({'message': 'Keys generated successfully'})

@app.route('/api/ecc/sign', methods=['POST'])
def ecc_sign_message():
    data = request.json
    message = data['message']
    private_key, _ = ecc_cipher.load_keys()
    signature = ecc_cipher.sign(message, private_key)
    signature_hex = signature.hex()
    return jsonify({'signature': signature_hex})

@app.route('/api/ecc/verify', methods=['POST'])
def ecc_verify_signature():
    data = request.json
    message = data['message']
    signature_hex = data['signature']
    public_key, _ = ecc_cipher.load_keys()
    signature = bytes.fromhex(signature_hex)
    is_verified = ecc_cipher.verify(message, signature, public_key)
    return jsonify({'is_verified': is_verified})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
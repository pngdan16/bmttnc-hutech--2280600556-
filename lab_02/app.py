from flask import Flask, render_template, request, jsonify
from cipher.caesar import CaesarCipher

app = Flask(__name__)
caesar = CaesarCipher()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/caesar')
def caesar_cipher():
    return render_template('caesar.html')

@app.route("/encrypt", methods=["POST"])
def caesar_encrypt():
    try:
        text = request.form['inputPlainText']
        key = int(request.form['inputKeyPlain'])
        encrypted_text = caesar.encrypt_text(text, key)
        return render_template('caesar.html', 
                            encrypted_result=encrypted_text,
                            plain_text=text,
                            encrypt_key=key)
    except Exception as e:
        return render_template('caesar.html', 
                            error="Encryption error: " + str(e),
                            plain_text=text if 'text' in locals() else "",
                            encrypt_key=key if 'key' in locals() else "")

@app.route("/decrypt", methods=["POST"])
def caesar_decrypt():
    try:
        text = request.form['inputCipherText']
        key = int(request.form['inputKeyCipher'])
        decrypted_text = caesar.decrypt_text(text, key)
        return render_template('caesar.html',
                            decrypted_result=decrypted_text,
                            cipher_text=text,
                            decrypt_key=key)
    except Exception as e:
        return render_template('caesar.html',
                            error="Decryption error: " + str(e),
                            cipher_text=text if 'text' in locals() else "",
                            decrypt_key=key if 'key' in locals() else "")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
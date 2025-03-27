import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Kết nối buttons với các hàm xử lý
        self.ui.pushButton.clicked.connect(self.call_api_encrypt)
        self.ui.pushButton_2.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        try:
            # Lấy dữ liệu từ UI
            plain_text = self.ui.textEdit.toPlainText()
            key = int(self.ui.lineEdit.text())  # Chuyển key thành số
            
            payload = {
                "plain_text": plain_text,
                "key": key
            }
            
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.lineEdit_2.setText(data['encrypted_message'])
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.exec_()
            else:
                QMessageBox.critical(self, "Error", f"API Error: {response.status_code}")
        except ValueError:
            QMessageBox.warning(self, "Warning", "Key must be a number")
        except requests.exceptions.ConnectionError:
            QMessageBox.critical(self, "Error", "Could not connect to server. Make sure the API server is running.")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Request Error: {str(e)}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Unexpected Error: {str(e)}")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        try:
            # Lấy dữ liệu từ UI
            cipher_text = self.ui.lineEdit_2.text()
            key = int(self.ui.lineEdit.text())  # Chuyển key thành số
            
            payload = {
                "cipher_text": cipher_text,
                "key": key
            }
            
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.textEdit.setText(data["decrypted_message"])
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                QMessageBox.critical(self, "Error", f"API Error: {response.status_code}")
        except ValueError:
            QMessageBox.warning(self, "Warning", "Key must be a number")
        except requests.exceptions.ConnectionError:
            QMessageBox.critical(self, "Error", "Could not connect to server. Make sure the API server is running.")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Request Error: {str(e)}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Unexpected Error: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
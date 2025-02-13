import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import ssl
import smtplib
from email.message import EmailMessage
from credentials import password
import random


def verification_code():
    pw = [str(random.randint(0, 9)) for i in range(6)]
    return "".join(pw)


class EmailVerificationUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Email Verification')
        self.setGeometry(100, 100, 400, 200)

        self.email_label = QLabel('Enter your email address:')
        self.email_input = QLineEdit()
        self.send_button = QPushButton('Send Verification Code')
        self.code_label = QLabel('Enter verification code:')
        self.code_input = QLineEdit()
        self.verify_button = QPushButton('Verify Email')
        self.sent_code = None

        layout = QVBoxLayout()
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.send_button)
        layout.addWidget(self.code_label)
        layout.addWidget(self.code_input)
        layout.addWidget(self.verify_button)

        self.setLayout(layout)

        self.send_button.clicked.connect(self.send_verification_code)
        self.verify_button.clicked.connect(self.verify_email)

    def send_verification_code(self):
        email_address = self.email_input.text()
        sender = "pooyanoveisi15@gmail.com"
        receiver = email_address
        subject = 'Your Verification Code'
        vc = verification_code()
        body = f"""
        Your code is {vc}
        """

        email = EmailMessage()
        email['From'] = sender
        email['To'] = receiver
        email['Subject'] = subject

        email.set_content(body)
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(sender, password)
            smtp.send_message(email)
            self.sent_code = vc
            self.code_label.setText('Verification code sent to your email address')

    def verify_email(self):
        verification_code = self.code_input.text()
        if verification_code == self.sent_code:
            QMessageBox.information(self, 'Verification', 'Verification was successful!')
        else:
            QMessageBox.error(self, 'Verification', 'Verification failed. Please try again.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EmailVerificationUI()
    window.show()
    sys.exit(app.exec_())

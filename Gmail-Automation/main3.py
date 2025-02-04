import ssl
import smtplib
from email.message import EmailMessage
from credentials import password

sender = "awrash.sn@gmail.com"
receiver = input("Enter your email address : ")
subject = 'فایل مشتریان'

body = f"""
اسامی مشتریان در فایل زیر آورده شده اند
"""

email = EmailMessage()  # sakht yek email
email['From'] = sender  # ferestande
email['To'] = receiver  # girande
email['Subject'] = subject  # onvan

email.set_content(body)

# Add file attachment
with open('customers.csv', 'rb') as file:
    # email.add_attachment(file.read(), maintype='csv', subtype='csv', filename=file.name)
    email.add_attachment(file.read(), maintype='csv', subtype='csv', filename="moshtarian.csv")


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(sender, password)  # login kardan be server smtp
    smtp.send_message(email)  # ersal email
    print("File has been sent")

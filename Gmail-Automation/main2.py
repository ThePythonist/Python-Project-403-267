import random
import smtplib, ssl
from credentials import password

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "arash.sn.work@gmail.com"
receiver_email = input("Enter your email address : ")


def verification_code():
    pw = [str(random.randint(0, 9)) for i in range(6)]
    return "".join(pw)


vc = verification_code()

message = f"""
You verification code is {vc}"""

context = ssl.create_default_context()

with smtplib.SMTP(smtp_server, port) as server:
    server.starttls(context=context)
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)


def verify():
    entry = input(f"Enter verification code sent to {receiver_email} : ")

    if entry == vc:
        print("Logged in")
    else:
        print("Incorrect verification code. Try again")
        verify()


verify()

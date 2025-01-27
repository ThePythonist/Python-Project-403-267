import smtplib, ssl
from credentials import password

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "arash.sn.work@gmail.com"
receiver_email = "s89748476@gmail.com"

message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()

with smtplib.SMTP(smtp_server, port) as server:
    server.starttls(context=context)
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

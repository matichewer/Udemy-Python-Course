# send_emai.py
import smtplib
import ssl
import os
from dotenv import load_dotenv

def send_email(message):    
    
    load_dotenv()
    username = os.getenv("EMAIL_SENDER")
    password = os.getenv("EMAIL_PASSWORD")
    receiver = os.getenv("EMAIL_RECEIVER")

    host = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()
    
    # Encode the message using UTF-8 for fix content emails
    message = message.encode("utf-8")

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

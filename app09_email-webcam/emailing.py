import smtplib
import os
from dotenv import load_dotenv
from email.message import EmailMessage
import imghdr 

def send_email(image_path):    
    
    print("Email: sending...")
        
    load_dotenv()
    sender = os.getenv("EMAIL_SENDER")
    password = os.getenv("EMAIL_PASSWORD")
    receiver = os.getenv("EMAIL_RECEIVER")        
    
    
    email_message = EmailMessage()
    email_message["Subject"] = "Objecto detectado!"
    email_message.set_content("Se ha detectado un nuevo objeto. Revisa la imagen adjunta.")
    
    with open(image_path, 'rb') as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))
    
    
    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(sender, password)
    gmail.sendmail(sender, receiver, email_message.as_string())
    gmail.quit()

    print("Email: sended!")

if __name__ == "__main__":
    send_email("images/4.png")
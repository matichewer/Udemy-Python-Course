import smtplib
import ssl
import os
import streamlit as st
from dotenv import load_dotenv

def load_email_credentials():
    try:
        # Intentar cargar las credenciales desde el archivo .env
        load_dotenv()
        username = os.getenv("EMAIL_SENDER")
        password = os.getenv("EMAIL_PASSWORD")
        receiver = os.getenv("EMAIL_RECEIVER")

        # Si no se encuentran en el archivo .env, cargar desde los secrets de Streamlit
        if username is None or password is None or receiver is None:
            print("Credenciales no encontradas en el archivo .env")
            raise ValueError("Credenciales no encontradas en el archivo .env")
    except Exception as e:
        # Capturar cualquier excepción durante la carga de las credenciales
        st.warning(f"Error al cargar las credenciales: {e}")
        print("Cargo las credenciales desde los secrets de Streamlit")
        # Intentar cargar desde los secrets de Streamlit
        username = st.secrets["EMAIL_SENDER"]
        password = st.secrets["EMAIL_PASSWORD"]
        receiver = st.secrets["EMAIL_RECEIVER"]

    return username, password, receiver

def send_email(message):
    username, password, receiver = load_email_credentials()

    host = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

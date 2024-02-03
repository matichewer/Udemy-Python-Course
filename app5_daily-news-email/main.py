# main.py
import requests
import os
from dotenv import load_dotenv
from send_email import send_email


# Intentar cargar las credenciales desde el archivo .env
load_dotenv()

topic = "tesla"
api_key = os.getenv("NEWS_API")
url = (
    "https://newsapi.org/v2/everything?"
    "q={topic}&"
    "from=2023-12-22&"
    "sortBy=publishedAt&"
    "apiKey=b9fce070a5ea4fabb926503d5d6dc63c&"
    "language=es"
)

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

message = f"Subject: News from Python!\n\n"

# Access the article with data
for article in content["articles"][:20]:
    if article["title"] is not None:
        # print(article["title"])
        # print(article["description"])

        message = (
            message
            + f"""
                Title: {article['title']}
                Description: {article['description']}
                Link: {article['url']}                
            """
        )

send_email(message)

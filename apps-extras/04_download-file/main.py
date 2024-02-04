import requests

url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Cat_August_2010-4.jpg/1920px-Cat_August_2010-4.jpg"

response = requests.get(url)

# Open in write binary mode
with open("image.jpg", "wb") as file:
    file.write(response.content)

print("File 'image.png' was downloaded")
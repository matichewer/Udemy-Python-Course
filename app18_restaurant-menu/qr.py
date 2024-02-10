import qrcode


image = qrcode.make("https://187.0.0.1:8000")
image.save("qr.png", "PNG")

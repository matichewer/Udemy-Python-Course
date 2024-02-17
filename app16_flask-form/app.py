from datetime import datetime
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from flask_mail import Mail, Message

app = Flask(__name__)

load_dotenv()
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = os.getenv("EMAIL_SENDER")
app.config["MAIL_PASSWORD"] = os.getenv("EMAIL_PASSWORD")

db = SQLAlchemy(app)

mail = Mail(app)


class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date)
    occupation = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Form('{self.first_name}', '{self.last_name}', '{self.email}', '{self.date}', '{self.occupation}')"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        date = request.form["date"]
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        occupation = request.form["occupation"]

        # Creamos una nueva fila en la base de datos
        form = Form(
            first_name=first_name,
            last_name=last_name,
            email=email,
            date=date_obj,
            occupation=occupation,
        )
        db.session.add(form)
        db.session.commit()

        message_body = (
            f"Hello {first_name}! \n\n"
            f"Here are your data: \n    {first_name}\n    {last_name}\n    {email}\n    {date}\n    {occupation}\n\n"
            f"Thanks for submitting the form! \n"
        )

        meesage = Message(
            subject="New form submission",
            sender=app.config["MAIL_USERNAME"],
            recipients=[email],
            body=message_body,
        )

        mail.send(meesage)

        flash(f"{first_name}, your form was submitted successfully! ", "success")

    return render_template("index.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # chequea que exista y sino crea la base de datos
        app.run(debug=False, host='0.0.0.0', port=5001)


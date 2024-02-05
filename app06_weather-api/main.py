from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def api(station, date):
    temperature = 23
    return {"station": station, "date": date, "temperature": temperature}


if __name__ == "__main__":
    app.run(debug=True, port=5000)
    print("Running app...")

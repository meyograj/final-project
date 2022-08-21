import flask
from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("aboutus.html")
@app.route("/home")
def home():
    return render_template("home.html")
@app.route("/ann")
def ann():
    return render_template("ann.html")
@app.route("/cnn")
def cnn():
    return render_template("cnn.html")
@app.route("/ml")
def ml():
    return render_template("ml.html")
@app.route("/rnn")
def rnn():
    return render_template("rnn.html")

if __name__ == "__main__":
    app.run(debug=True)
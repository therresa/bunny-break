from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["GET", "POST"])
def chat():
    inp = request.form.get('text-chat')
    


from flask import Flask
import opszero_rustypy

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World with Python Flask!"


@app.route("/rust")
def rust():
    return opszero_rustypy.sum_as_string(1, 2)


app.run(host="0.0.0.0", port=81)

import re
from flask import Flask,render_template,send_file
import os
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/strings/<file_name>")
def strings(file_name):
    return send_file('./strings/'+file_name)

@app.route("/evolve/<file_name>")
def evolve(file_name):
    return send_file('./evolve/'+file_name)

if __name__ == "__main__":
    app.run()
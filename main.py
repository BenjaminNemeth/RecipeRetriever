import time

from flask import Flask, render_template, url_for, request
import requests
import json
import sys

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("WelcomePage.html")


@app.route("/main", methods=["GET", "POST"])
def mainPage():
    if request.method == 'POST':
        time.sleep(1)
        return render_template('resultsPage.html')

    return render_template("main.html")


@app.route('/processUserInput/<string:userData>', methods=['POST'])
def processInput(userData):
    userInput = json.loads(userData)
    print("hi")
    print(userInput)
    return render_template("resultsPage.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)

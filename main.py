from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("WelcomePage.html")


@app.route("/main", methods=["GET", "POST"])
def mainPage():
    return render_template("main.html")



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)


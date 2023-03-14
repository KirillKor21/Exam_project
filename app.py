from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/main")
def main():
    return render_template("main.html")

@app.route("/fall")
def fall():
    return render_template("fall.html")

if __name__ == "__main__":
    app.run()

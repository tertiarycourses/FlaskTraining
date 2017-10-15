# Python Flask Essential Training
# Module 2: Templating
# Control flow

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index4.html",fruit="apple")

if __name__ == "__main__":
  app.run()
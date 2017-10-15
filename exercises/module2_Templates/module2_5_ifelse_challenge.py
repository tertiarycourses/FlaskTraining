# Python Flask Essential Training
# Module 2: Templating
# Pass variable to template

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index4_challenge.html",today=30)

if __name__ == "__main__":
  app.run()
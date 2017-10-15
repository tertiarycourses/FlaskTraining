# Python Flask Essential Training
# Module 2: Templating
# For loop

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	title = "Learning Flask"
	paragraph = "Flask is awesome"
	return render_template("index5.html",title=title, paragraph=paragraph)

if __name__ == "__main__":
  app.run()
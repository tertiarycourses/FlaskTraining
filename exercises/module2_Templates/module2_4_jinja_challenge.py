# Python Flask Essential Training
# Module 2: Templating
# Jinga templating

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	title = "Learning Flask"
	text = "Awesome day, learn a lot of stuff"
	return render_template("index3.html",title=title,text=text)

if __name__ == "__main__":
  app.run()
# Python Flask Essential Training
# Module 2: Templating
# For loop over dictionary

from flask import Flask, render_template

content = { "Fruits":['Apple','Orange','Banana'],
			"Animals":['Cat','Dog','Elephant']}

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index6.html",content=content)

if __name__ == "__main__":
  app.run()
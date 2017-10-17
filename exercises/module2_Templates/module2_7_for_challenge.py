# Python Flask Essential Training
# Module 2: Templating
# For loop over dictionary

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
	person = {"Ally":"apple","Alfred":"durian"}
	return render_template("index6.html",person=person)

if __name__ == "__main__":
  app.run()
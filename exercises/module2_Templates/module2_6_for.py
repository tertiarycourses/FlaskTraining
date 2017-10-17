# Python Flask Essential Training
# Module 2: Templating
# For loop

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
	person = ["Ally", "Alfred"]
	return render_template("index5.html", person=person)

if __name__ == "__main__":
    app.run(debug=True)

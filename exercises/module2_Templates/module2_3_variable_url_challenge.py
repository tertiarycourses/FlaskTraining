# Python Flask Essential Training
# Module 2: Templating
# Pass variable from URL

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/aboutus")
def index():
	title = "About Us"
	text = "We are established in 2012"
	return render_template("index2_challenge.html",title=title,text=text)

if __name__ == "__main__":
  app.run()
# Python Flask Essential Training
# Module 2: Templating
# Render template

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/aboutus")
def aboutus():
  return render_template("aboutus.html")

if __name__ == "__main__":
  app.run(port=5004)
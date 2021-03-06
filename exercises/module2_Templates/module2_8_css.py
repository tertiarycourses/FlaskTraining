# Python Flask Essential Training
# Module 2: Templating
# CSS Styling

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index7.html")

if __name__ == "__main__":
  app.run(port=5002)
# Python Flask Essential Training
# Module 2: Templating
# Add variable to template

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index2.html",title="Flask",paragraph="Awesome")

if __name__ == "__main__":
  app.run()
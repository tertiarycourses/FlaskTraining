# Python Flask Essential Training
# Module 2: Templating
# For loop challenge

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<list>")
def index(list):
  return render_template("index5_challenge.html",list=list)

if __name__ == "__main__":
  app.run()
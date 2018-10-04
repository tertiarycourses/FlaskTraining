# Python Flask Essential Training
# Module 3: Request
# Redirect URL

from flask import Flask, flash, render_template
app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route('/')
def index():
   flash('Hello this is a flash')
   return render_template('index3.html')

if __name__ == '__main__':
   app.run()



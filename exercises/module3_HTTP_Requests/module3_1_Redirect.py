# Python Flask Essential Training
# Module 3: HTTP Request
# Redirect URL

from flask import Flask, url_for,redirect
app = Flask(__name__)

@app.route('/')
def index():
   return redirect('http://www.google.com')
   #return redirect(url_for('login'))

@app.route('/login')
def login():
   return "Login Page"

if __name__ == '__main__':
   app.run()
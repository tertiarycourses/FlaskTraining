# Python Flask Essential Training
# Module 3: HTTP Request
# POST method

from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   return 'welcome {}'.format(name)

@app.route('/login',methods = ['GET','POST'])
def login():
	if request.method == 'POST':
		user = request.form['username']
		return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(port=5005)
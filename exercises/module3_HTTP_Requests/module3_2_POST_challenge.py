# Python Flask Essential Training
# Module 3: HTTP Request
# POST method

from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        score = request.form['score']
        return render_template('success.html',user = user,score= score)

if __name__ == '__main__':
   app.run()
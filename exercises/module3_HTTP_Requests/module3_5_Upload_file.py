# Python Flask Essential Training
# Module 3: HTTP Request
# File Upload

from flask import Flask, render_template, request
# from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/uploader',methods = ['GET','POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['file']
		f.save(f.filename)
		return 'file uploaded successfully'

@app.route('/upload')
def upload():
   return render_template('upload_file.html')

if __name__ == '__main__':
   app.run()
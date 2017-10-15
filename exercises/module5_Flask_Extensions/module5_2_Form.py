# Python Flask Essential Training
# Module 5: Flask Extensions
# Mail Extension


from flask import Flask, render_template
from forms import ContactForm
app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/contact')
def contact():
   form = ContactForm()
   return render_template('contact.html', form = form)

@app.route('/success')
def success():
   return render_template('success.html')

if __name__ == '__main__':
   app.run()

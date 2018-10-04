from flask import Flask
app = Flask(__name__)

@app.route("/hello/<user>")
def hello(user ):
    return "Hello %s" %user

@app.route('/hello2/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

if __name__ == "__main__":
    app.run()

# use another port
# if __name__ == "__main__":
#     app.run(port='5001')
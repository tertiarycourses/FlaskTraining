from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/hello2')
def hello2():
    return 'Hello, World 2!'

if __name__ == "__main__":
    app.run()
from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def hi():
    return "Hello world"

@app.route('/about')
def about():
    return "this is about page"


if __name__ == "__main__":
    app.run(port=None)

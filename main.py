from flask import Flask, request, render_template
from jinja2 import Template
import json

app = Flask(__name__)



@app.route('/')
@app.route('/home')
def home():
    foydalanuvchi = {
        "name": "Javohir",
        "age": 10,
    }
    return render_template('home.html', user = foydalanuvchi)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    contacts = [
        {
            "name": "Farrux",
            "tel": '+9862636453'
        },
        {
            "name": "Sanjar",
            "tel": '+65465165'
        },
        {
            "name": "Javohir",
            "tel": '+65462222225165'
        },
        {
            "name": "Bobur",
            "tel": '+999999965165'
        }
    ]
    return render_template('contact.html', contacts = contacts)


if __name__ == "__main__":
    app.run(port=None)

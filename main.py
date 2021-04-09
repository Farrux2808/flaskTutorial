from flask import Flask, request, render_template
from jinja2 import Template
import json
from tinydb import TinyDB, Query

app = Flask(__name__)

db = TinyDB('db.json')
table_products = db.table('products')
productQuery = Query()

@app.route('/')
@app.route('/home')
def home():
    products = table_products.all()
    return render_template('home.html', products = products)

@app.route('/product')
def product():
    r = request.args
    product = table_products.search(productQuery.ID == r['id'])
    return render_template('product.html', aaaa = product[0])









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

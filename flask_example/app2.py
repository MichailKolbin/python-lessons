from flask import Flask, render_template

app = Flask(__name__)

# Sample list of products
products = [
    {"name": "Product 1", "price": 10},
    {"name": "Product 2", "price": 20},
    {"name": "Product 3", "price": 30},
    {"name": "Product 4", "price": 40},
    {"name": "Product 5", "price": 50}
]


@app.route('/')
def index():
    return render_template('index2.html', products=products)


if __name__ == '__main__':
    app.run(debug=True)

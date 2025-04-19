from flask import Flask, jsonify
from models.schema import Product, db

app = Flask(__name__)


@app.route("/products", methods=["GET"])
def get_products():
    db.connect()
    products = [
        {
            "id": p.id,
            "title": p.title,
            "price": p.price,
            "url": p.url,
            "rating": p.rating
        }
        for p in Product.select()
    ]
    db.close()
    return jsonify(products)


if __name__ == "__main__":
    app.run(debug=True)

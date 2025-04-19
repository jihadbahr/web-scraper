from models.schema import Product, db


def save_to_db(products):
    db.connect()
    db.create_tables([Product], safe=True)

    with db.atomic():
        for product in products:
            existing_product = Product.get_or_none(Product.url == product["url"])

            if existing_product:
                existing_product.title = product["title"]
                existing_product.price = product["price"]
                existing_product.rating = product["rating"]
                existing_product.save()
            else:
                Product.create(
                    title=product["title"],
                    price=product["price"],
                    url=product["url"],
                    rating=product["rating"]
                )

    db.close()

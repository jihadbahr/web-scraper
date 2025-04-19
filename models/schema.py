import os
from peewee import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(BASE_DIR, 'products.db')
db = SqliteDatabase(db_path)


class Product(Model):
    id = AutoField()
    title = CharField()
    price = FloatField(null=True)
    url = TextField(unique=True)
    rating = IntegerField(null=True)

    class Meta:
        database = db

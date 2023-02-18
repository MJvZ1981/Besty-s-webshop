# Models go here
from peewee import *

db = SqliteDatabase('webshop.db', pragmas={'foreign_keys': 1})

class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    user_id=AutoField()
    name=TextField()
    adress=TextField()
    billing_info=IntegerField()


class Product(BaseModel):
    product_id=AutoField()
    owner=ForeignKeyField(User, backref='products')
    name=TextField()
    description=TextField()
    price=DecimalField(decimal_places=2)
    quantity=IntegerField(null=True)
    tags=TextField()


class Tag(BaseModel):
    tag_id=AutoField()
    name=TextField()
    

class Transaction(BaseModel):
    product=ForeignKeyField(Product, backref='product')
    bought_id=AutoField()
    buyer=ForeignKeyField(User, backref='buyer')
    amount=IntegerField(null=True)
    date=DateField()
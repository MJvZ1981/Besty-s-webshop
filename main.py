__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import *
from peewee import *
import datetime


def search(term):
    return print([i.name for i in Product.select().where(Product.name.contains(term.lower())|Product.description.contains(term.lower()))])


def list_user_products(user_id):
    return print([i.name for i in Product.select().where(Product.owner == user_id)])


def list_products_per_tag(tag_id):
    tag = Tag.get_by_id(tag_id)
    return print([i.name for i in Product.select().where(Product.tags.contains(tag.name))]) 


def add_product_to_catalog(user_id, product):
    user_id = user_id
    product = Product.get_or_create(
        name = product,
        description = input('description: '),
        price = input('price: '),
        quantity = input('amount: '),
        owner = user_id,
        tags = input('tags: ')
    )
    print('The following has been added to the catalog: ')
    query = Product.select().where(Product.product_id == Product.select(fn.MAX(Product.product_id)).scalar())
    for i in query:
        print(i.name, i.description, i.price, i.quantity, i.owner, i.tags)


def update_product_name(product_id, new_name):
    try:
        product = Product.get_by_id(product_id)
        product.name = new_name
        product.save()
    except DoesNotExist:
        print('ERROR: Product does not exist')


def update_description(product_id, new_description):
    try:
        product = Product.get_by_id(product_id)
        product.description = new_description
        product.save()
    except DoesNotExist:
        print('ERROR: Product does not exist')


def update_price(product_id, new_price):
    try:
        product = Product.get_by_id(product_id)
        product.price = new_price
        product.save()
    except DoesNotExist:
        print('ERROR: Product does not exist')


def update_stock(product_id, new_quantity):
    try:
        product = Product.get_by_id(product_id)
        product.quantity = new_quantity
        product.save()
    except DoesNotExist:
        print('ERROR: Product does not exist')


def update_tag(tag_id, name):
    try:
        tag = Tag.get_by_id(tag_id)
        tag.name = name
        tag.save()
    except DoesNotExist:
        print('ERROR: Product does not exist')


def add_tag_to_product(product_id, new_tag):
    try:
        product = Product.get_by_id(product_id)
        product.tags = new_tag
        product.save()
    except DoesNotExist:
        print('ERROR: Product does not exist')

    
def add_tag_to_tags():
    tag = Tag.get_or_create(name = input('tag name: '))
    return tag


def purchase_product(product_id, buyer_id, quantity):
    try:
        product = Product.get_by_id(product_id)
        buyer_id = User.get_by_id(buyer_id)
        if product.owner != buyer_id:
            if product.quantity >= quantity:
                product.quantity -= quantity
                product.save()
                Transaction.create(
                    product = product_id,
                    buyer = buyer_id,
                    amount = quantity,
                    date = datetime.datetime.now()
                )
            else:
                print('ERROR: Not enough stock')
        else:
            print('ERROR: You are the owner of this product')
    except DoesNotExist:
        print('ERROR: Product does not exist')
    

def show_product_database():
    query = Product.select()
    for i in query:
        print(i.name, i.description, i.price, i.quantity, i.owner, i.tags)

    
def show_user_database():
    query = User.select()
    for i in query:
        print(i.user_id, i.name, i.adress, i.billing_info)


def remove_product(product_id):
    try:
        product = Product.get_by_id(product_id)
        product.delete_instance()
    except DoesNotExist:
        print('ERROR: Product does not exist')


def show_transactions():
    query = Transaction.select()
    for i in query:
        print(i.product, i.bought_id, i.buyer, i.amount, i.date)


if __name__ == "__main__":
    # search('ch')
    # list_user_products(1)
    # list_products_per_tag(8)
    # add_product_to_catalog(8, 'chocolate bar')
    # update_product_name(17, 'chocolate bar')
    # update_description(17, 'home-made chocolat bar, 100% organic')
    # update_price(17, 4.50)
    # update_stock(17, 25)
    # update_tag(43, '100% organic')
    # add_tag_to_product(17, 'sweet')
    # add_tag_to_tags()
    # purchase_product(1, 3, 1)
    # show_product_database()
    # show_user_database()
    # remove_product(18)
    # print(show_transactions())
    ...
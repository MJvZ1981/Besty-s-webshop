from models import *


def populate_test_database():

    db.connect()

    db.create_tables([User, Product, Transaction, Tag])
    
    users = [
        {'name': 'Alby Onestone', 'adress': 'Alblasterdamn 1, Albertville', 'billing_info': 5049382716},
        {'name': 'Icy Newton', 'adress': 'Newtonstreet 2, Newtopia', 'billing_info': 1092387456},
        {'name': 'Jane Doe', 'adress': 'Janeslane 3, Janeville', 'billing_info': 1234567890},
        {'name': 'John Doe', 'adress': 'Johnsonstreet 4, Johnnyville', 'billing_info': 16273849506},
        {'name': 'Kanye Western', 'adress': 'Westturn 5, Westside Story', 'billing_info': 6172839405},
        {'name': 'Nicole Tessler', 'adress': 'Wardenclyffestreet 6, Tulsa', 'billing_info': 1029384756},
        {'name': 'Pamela Andhersons', 'adress': 'Buchannonstreet 7, Saint Mitchell', 'billing_info': 1209348756},
        {'name': 'Willy Wonker', 'adress': 'Dahlstreet 8, Roal Madrid', 'billing_info': 2468097531}
    ]
    
    products = [
        {'owner': 1, 'name': 'necklace', 'description': 'self-made necklace, made with crystals', 'price': 49.95, 'quantity': 25, 'tags': ['jewelry', 'accessory', 'vintage', 'crystal']},
        {'owner': 1, 'name': 'bracelet', 'description': 'self-made bracelet, made with amberstone', 'price': 15.95, 'quantity': 50, 'tags': ['jewelry', 'accessory', 'vintage', 'amberstone']},
        {'owner': 2, 'name': 'remote-control car', 'description': 'self-made car from garbage', 'price': 29.95, 'quantity': 40, 'tags': ['remote-control car', 'toy', 'electronic']},
        {'owner': 2, 'name': 'robot-head', 'description': 'robot that recites Newton quotes', 'price': 39.95, 'quantity': 10, 'tags': ['robot', 'Newton', 'tech']},
        {'owner': 3, 'name': 'slippers', 'description': 'self-made woolen slippers', 'price': 15.95, 'quantity': 30, 'tags': ['slippers', 'wool', 'homewear']},
        {'owner': 3, 'name': 'socks', 'description': 'self-made woolen socks', 'price': 15.95, 'quantity': 10, 'tags': ['socks', 'wool', 'winterwear']},
        {'owner': 4, 'name': 'clock', 'description': 'self-made wooden clock', 'price': 95.95, 'quantity': 8, 'tags': ['clock', 'wood']},
        {'owner': 4, 'name': 'watches', 'description': 'watch with a compass', 'price': 45.95, 'quantity': 20, 'tags': ['watch', 'accessory', 'compass']},
        {'owner': 5, 'name': 'mixed tape', 'description': 'mixed-tape with songs from the best musicals', 'price': 19.95, 'quantity': 25, 'tags': ['tape', 'songs', 'musical']},
        {'owner': 5, 'name': 'sandals', 'description': 'scandalous great sandals', 'price': 75.95, 'quantity': 10, 'tags': ['sandals', 'hip', 'trendy', 'footwear']},
        {'owner': 6, 'name': 'batter eat', 'description': 'charge yourself with this nutricious batter', 'price': 15.95, 'quantity': 10, 'tags': ['food', 'superfood', 'nutricious']},
        {'owner': 6, 'name': 'electronic buggy', 'description': 'anti-gravity buggy that floats', 'price': 245.95, 'quantity': 10, 'tags': ['buggy', 'hi-tech', 'wood', 'anti-gravity']},
        {'owner': 7, 'name': 'silicone molds', 'description': 'unique shapes for baking', 'price': 15.95, 'quantity': 20, 'tags': ['baking', 'shapes', 'silicone']},
        {'owner': 7, 'name': 'silicone art', 'description': 'self-made arty silicone molds', 'price': 20.00, 'quantity': 10, 'tags': ['silicone', 'art', 'shapes', 'unique']},
        {'owner': 8, 'name': 'chocolate cake', 'description': 'home-made chocolate cake with nuggets', 'price': 14.95, 'quantity': 10, 'tags': ['chocolate', 'food',  'cake', 'baking']},
        {'owner': 8, 'name': 'chocolate pudding', 'description': 'home-made chocolate pudding (pure)', 'price': 9.95, 'quantity': 5, 'tags': ['chocolate', 'food', 'pudding', 'dessert', 'baking']}
    ]

    for user in users:
        User.create(name=user['name'], adress=user['adress'], billing_info=user['billing_info'])

    for product in products:
        Product.create(owner=product['owner'], name=product['name'], description=product['description'], price=product['price'], quantity=product['quantity'], tags=product['tags'])

    tags = []

    for product in products:
        for tag in product['tags']:
            if tag not in tags:
                tags.append(tag)

    for tag in tags:
        Tag.create(name=tag) 


    db.close()


if __name__ == '__main__':
    populate_test_database()
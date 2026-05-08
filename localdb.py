
from typing import List
from models import Product

# This file contains a list of products that we will use to initialize the database with some sample data. The products are represented as instances of the Product model, which is defined in the models.py file. Each product has an id, name, description, price, and quantity. This localdb.py file allows us to easily manage and update the sample data for our application without having to modify the database directly.
products: List[Product] = [
    Product(
        id=1,
        name="iPhone 15",
        description="Apple smartphone",
        price=79999,
        quantity=10
    ),
    Product(
        id=2,
        name="Samsung S24",
        description="Samsung flagship phone",
        price=74999,
        quantity=8
    ),
    Product(
        id=3,
        name="MacBook Air",
        description="Apple laptop M2",
        price=114999,
        quantity=5
    ),
    Product(
        id=4,
        name="Sony Headphones",
        description="Noise cancelling headphones",
        price=19999,
        quantity=15
    ),
    Product(
        id=5,
        name="Logitech Mouse",
        description="Wireless gaming mouse",
        price=2999,
        quantity=20
    ),
]
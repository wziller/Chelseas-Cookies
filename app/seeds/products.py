from app.models import db, Review, User
from werkzeug.security import generate_password_hash
from faker import Faker
from random import randint, uniform

from app.models.product import Product

fake = Faker()

adjectives = [
    'appealing',
    'appetizing',
    'aromatic',
    'baked',
    'beautiful',
    'bite-size',
    'blazed',
    'blended',
    'brown',
    'burnt',
    'buttered',
    'caked',
    'candied',
    'caramelized',
    'cheesy',
    'chocolate',
    'cholesterol free',
    'chunked',
    'classic',
    'classy',
    'creamed',
    'creamy',
    'crisp',
    'crunchy',
    'dazzling',
    'deep-fried',
    'delectable',
    'delicious',
    'delight',
    'distinctive',
    'doughy',
    'dressed',
    'dripping',
    'drizzle',
    'dry',
    'dull',
    'edible',
    'elastic',
    'extraordinary',
    'fantastic',
    'filet',
    'fizzy',
    'flaky',
    'flat',
    'flavored',
    'flavorful',
    'fleshy',
    'fluffy',
    'fresh',
    'fried',
    'frozen',
    'fruity',
    'furry',
    'generous',
    'gingery',
    'glazed',
    'golden',
    'gorgeous',
    'gourmet',
    'greasy',
    'grilled',
    'gritty',
    'harsh',
    'heady',
    'honey',
    'hot',
    'icy',
    'infused',
    'insipid',
    'intense',
    'juicy',
    'jumbo',
    'kosher',
    'large',
    'lavish',
    'lean',
    'lite',
    'lively',
    'low',
    'low-fat',
    'luscious',
    'mashed',
    'mellow',
    'mild',
    'minty',
    'mixed',
    'moist',
    'moist',
    'mouth-watering',
    'natural',
    'non-fat',
    'nutmeg',
    'nutty',
    'organic',
    'petite',
    'piquant',
    'plain',
    'pleasant',
    'plump',
    'pureed',
    'rich',
    'robust',
    'saline',
    'salty',
    'savory',
    'sapid',
    'saporific',
    'saporous',
    'satin',
    'satiny',
    'savory',
    'scrumptious',
    'sea salt',
    'seasoned',
    'silky',
    'small',
    'smooth',
    'smothered',
    'soothing',
    'sour',
    'southern style',
    'special',
    'spiced',
    'spongy',
    'sprinkled',
    'stale',
    'steamed',
    'steamy',
    'sticky',
    'strawberry-flavored',
    'strong',
    'stuffed',
    'succulent',
    'sugar coated',
    'sugar free',
    'sugared',
    'sugarless',
    'sugary',
    'superb',
    'sweet',
    'sweet-and-sour',
    'sweetened',
    'syrupy',
    'tangy',
    'tantalizing',
    'tart',
    'tasteful',
    'tasty',
    'tender',
    'terrific',
    'thick',
    'thin',
    'toasted',
    'topped',
    'traditional',
    'treacly',
    'vanilla',
    'vanilla flavored',
    'velvety',
    'warm',
    'whipped',
    'whole',
    'wonderful',
    'yummy',
    'zesty',
    'zingy']

categories = [
        'Cake',
        'Cookie Cake',
        'Brownie',
        'Cinnamon Roll',
        'Doughnut',
        'Biscuit',
        'Bagel',
        'Bread',
        'Cookie',
        'Macaron',
        'Vegan Cake',
        'Vegan Cookie',
        'Cupcakes',
        'Muffins',
        'Cheesecake',
        ]

images = [
    "https://wziller-chelseas-cookies.s3.us-east-2.amazonaws.com/menu-vanilla-cupcake.png",
    "https://wziller-chelseas-cookies.s3.us-east-2.amazonaws.com/menu-sandwich-cookies-red-velvet.png",
    "https://wziller-chelseas-cookies.s3.us-east-2.amazonaws.com/menu-sandwich-cookies-carrot-cake.png",
    "https://wziller-chelseas-cookies.s3.us-east-2.amazonaws.com/menu-monster-cookie-1.png",
    "https://wziller-chelseas-cookies.s3.us-east-2.amazonaws.com/menu-homestyle-sugar.png",
    "https://wziller-chelseas-cookies.s3.us-east-2.amazonaws.com/menu-homestyle-shortbread.png",
    "https://wziller-chelseas-cookies.s3.us-east-2.amazonaws.com/menu-homestyle-red-velvet.png",
    "https://wziller-chelseas-cookies.s3.us-east-2.amazonaws.com/menu-homestyle-poppyseed-thumbprint.png",
    "https://wziller-chelseas-cookies.s3.us-east-2.amazonaws.com/menu-homestyle-peanut-butter.png",
    "https://wziller-chelseas-cookies.s3.us-east-2.amazonaws.com/menu-homestyle-oatmeal-raisin.png",
    "https://wziller-chelseas-cookies.s3.us-east-2.amazonaws.com/menu-homestyle-mexican-wedding.png",
    "https://wziller-chelseas-cookies.s3.us-east-2.amazonaws.com/menu-homestyle-double-chocolate-pecan.png",
    "https://wziller-chelseas-cookies.s3.us-east-2.amazonaws.com/menu-homestyle-coconut-macaroon.png",
    "https://wziller-chelseas-cookies.s3.us-east-2.amazonaws.com/menu-homestyle-chocolate-mexican-wedding.png",
    "https://wziller-chelseas-cookies.s3.us-east-2.amazonaws.com/menu-homestyle-chocolate-coconut-macaroon.png",
    "https://wziller-chelseas-cookies.s3.us-east-2.amazonaws.com/menu-homestyle-almond-toffee-crunch.png",
    "https://wziller-chelseas-cookies.s3.us-east-2.amazonaws.com/menu-giant-white-chocolate-macadamia.png",
    "https://wziller-chelseas-cookies.s3.us-east-2.amazonaws.com/menu-giant-smores.png",
    "https://wziller-chelseas-cookies.s3.us-east-2.amazonaws.com/menu-giant-molassas.png",
    "https://wziller-chelseas-cookies.s3.us-east-2.amazonaws.com/menu-giant-mm.png",
    "https://wziller-chelseas-cookies.s3.us-east-2.amazonaws.com/menu-giant-gf-snickerdoodle.png",
    "https://wziller-chelseas-cookies.s3.us-east-2.amazonaws.com/menu-cookie-cc.png",
    "https://wziller-chelseas-cookies.s3.us-east-2.amazonaws.com/menu-chocolate-cupcake.png",
    "https://wziller-chelseas-cookies.s3.us-east-2.amazonaws.com/menu-bars-snickers-brownie.png",
    "https://wziller-chelseas-cookies.s3.us-east-2.amazonaws.com/menu-bars-snickerdoodle-blondie.png",
    "https://wziller-chelseas-cookies.s3.us-east-2.amazonaws.com/menu-bars-raspberry-crumble.png",
    "https://wziller-chelseas-cookies.s3.us-east-2.amazonaws.com/menu-bars-pecan-pie.png",
    "https://wziller-chelseas-cookies.s3.us-east-2.amazonaws.com/menu-bars-lemon.png",
    "https://wziller-chelseas-cookies.s3.us-east-2.amazonaws.com/menu-bars-hello-dolly.png",
    "https://wziller-chelseas-cookies.s3.us-east-2.amazonaws.com/menu-bars-brownies.png"
]

def fake_name_generator(adjectives, categories, category_id):
    name = categories[category_id]
    adjective_count = randint(1,3)
    for _ in range(adjective_count):
        adjective = adjectives[randint(0,165)].capitalize()
        name = adjective + ' ' + name
    return name

# Adds a demo user, you can add other users here if you want
def seed_products():

    for _ in range(50):
        fake_description = fake.text(randint(100,800))
        fake_price = round(uniform(1.99,49.99), 2)
        category_id = randint(0,14)
        new_Product = Product(
            name = fake_name_generator(adjectives, categories, category_id),
            description = fake_description,
            price = fake_price,
            image_link = images[randint(0,24)],
            category = category_id + 1
            )
        db.session.add(new_Product)


    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_products():
    db.session.execute('TRUNCATE reviews RESTART IDENTITY CASCADE;')
    db.session.commit()

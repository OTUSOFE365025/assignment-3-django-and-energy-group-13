############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True

# Import settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# setup django environment
import django
django.setup()

# Import your models for use in your script
from db.models import *
from db.views import *

# Import flask
from flask import Flask

############################################################################
## START OF APPLICATION
############################################################################
""" Replace the code below with your own """

# Seed a few users in the database
# User.objects.create(name='Dan')
# User.objects.create(name='Robert')

# for u in User.objects.all():
#     print(f'ID: {u.id} \tUsername: {u.name}')
    
# Populate products table
# Product.objects.create(upc_code='012345678901', name='Wireless Mouse', price=24.99)
# Product.objects.create(upc_code='012345678902', name='Mechanical Keyboard', price=79.99)
# Product.objects.create(upc_code='012345678903', name='USB-C Charger 65W', price=34.50)
# Product.objects.create(upc_code='012345678904', name='Bluetooth Headphones', price=59.99)
# Product.objects.create(upc_code='012345678905', name='HDMI Cable 6ft', price=12.99)
# Product.objects.create(upc_code='012345678906', name='External Hard Drive 1TB', price=64.99)
# Product.objects.create(upc_code='012345678907', name='Laptop Stand', price=29.99)
# Product.objects.create(upc_code='012345678908', name='Webcam 1080p', price=45.00)
# Product.objects.create(upc_code='012345678909', name='Portable SSD 512GB', price=89.99)
# Product.objects.create(upc_code='012345678910', name='Gaming Mouse Pad', price=19.99)
# Product.objects.create(upc_code='012345678911', name='Wireless Earbuds', price=49.99)
# Product.objects.create(upc_code='012345678912', name='Smartphone Tripod', price=22.49)
# Product.objects.create(upc_code='012345678913', name='Power Bank 10000mAh', price=39.99)
# Product.objects.create(upc_code='012345678914', name='Smartwatch Band', price=14.99)
# Product.objects.create(upc_code='012345678915', name='LED Desk Lamp', price=27.95)
# Product.objects.create(upc_code='012345678916', name='Ergonomic Chair Cushion', price=32.00)
# Product.objects.create(upc_code='012345678917', name='Noise Cancelling Headset', price=89.50)
# Product.objects.create(upc_code='012345678918', name='Wireless Keyboard Combo', price=54.99)
# Product.objects.create(upc_code='012345678919', name='HD Monitor 24-inch', price=149.99)
# Product.objects.create(upc_code='012345678920', name='USB Flash Drive 128GB', price=18.49)

# for p in Product.objects.all():
#     print(f'UPC Code: {p.upc_code} \tProduct: {p.name} \t\tPrice: {p.price}')

# FLASK SERVER
app = Flask(__name__)

app.add_url_rule('/', 'search', search_product_flask)

if __name__ == '__main__':
    app.run(debug=True)
:rocket: Quick Setup
--------------------
Create a folder for your project on your local machine
```
mkdir myproject; cd myproject
```
Create a virtual environment and install django
```
python -m venv venv; source venv/bin/activate; pip install django
```
Download this project template from GitHub
```
git clone git@github.com:dancaron/Django-ORM.git; cd Django-ORM
```
Initialize the database
```
python manage.py makemigrations db; python manage.py migrate
```
Run the project
```
python main.py
```

Models:
-------
Product:
- upc_code(charfield): Stores the upc code of the product.
- name(charfield): Stores the name of the product.
- price(decimalfield): Stores the price of the product.

(didn't touch the default models and database instantiations)
User:
- name(charfield): Name of the user.

View:
------
search_product_flask: This view gets the entered upc_code through the browser's get functionality and tries to retrieve a product with the same upc code as the request.

Template:
---------
search.html: This is used for the search_product_flask view.

Static:
-------
styles.css: Used to style the search.html template.

Flask Server:
-------------
A flask server is run in main.py and our view is routed to the base url.

from flask import render_template, request
from .models import Product

def search_product_flask():
    query = request.args.get('upc_code', '')
    product = None
    error = None

    if query:
        try:
            product = Product.objects.get(upc_code=query)
        except Product.DoesNotExist:
            error = "No product found for that UPC."

    return render_template('search.html', product=product, error=error, query=query)

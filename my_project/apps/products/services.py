def get_product_details(product):
    return {
        'name': product.name.capitalize(),
        'description': product.description,
        'price': product.price,
        'in_stock': 'in stock' if product.in_stock > 0 else 'out of stock',
    }
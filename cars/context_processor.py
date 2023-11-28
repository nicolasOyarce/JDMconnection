from .cart import *

def total_cart_value(request):
    cart = request.session.get("cart", {})
    total_value = 0

    for key, value in cart.items():
        price = int(value.get("price", 0))
        quantity = int(value.get("quantity", 0))
        total_value += price 

    return {'total_cart_value': total_value}
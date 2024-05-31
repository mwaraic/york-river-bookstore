from .cart import Cart
from bookstore.apps.yrb.models import YrbShipping

def cart_total_amount(request):
    if request.user.is_authenticated:
        cart = Cart(request)
        total_bill = 0.0
        total_weight = 0.0
        for key, value in request.session['cart'].items():
            total_bill += float(value['price']) * value['quantity']
            total_weight += float(value['weight']) * value['quantity']

        # Calculate shipping cost based on total weight
        shipping_cost = 0.0
        for weight_range in range(1, 1001, 500):
            if total_weight <= weight_range:
                shipping_cost = YrbShipping.objects.get(weight=weight_range).cost
                break
        else:  # If total_weight exceeds the last weight range
            shipping_cost = YrbShipping.objects.last().cost

        # Return the cart subtotal, total amount, and shipping cost
        return {
            'cart_subtotal_amount': total_bill,
            'cart_total_amount': total_bill + float(shipping_cost),
            'cart_shipping': shipping_cost
        }
    else:
        return {
            'cart_subtotal_amount': 0,
            'cart_total_amount': 0,
            'cart_shipping': 0
        }

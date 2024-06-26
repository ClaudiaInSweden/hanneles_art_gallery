from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):

    cart_items = []
    total = 0
    delivery = 0

    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        delivery = 40
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context

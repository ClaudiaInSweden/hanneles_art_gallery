from django.shortcuts import (
    render, redirect, reverse, HttpResponse,
    get_object_or_404
)
from django.contrib import messages

from products.models import Product


def view_cart(request):

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        messages.info(request, f'Painting "{ product.name }"' +
                      ' is already in your shopping cart!')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Painting "{ product.name }"' +
                         ' has been added to your shopping cart.')
    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request, item_id):

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] += quantity
    else:
        cart.pop[item_id]

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):

    try:
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart', {})
        cart.pop(item_id)
        messages.info(request, f'Painting "{ product.name }"' +
                      ' has been removed from your shopping cart.')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Painting could not be removed: {e}')
        return HttpResponse(status=500)

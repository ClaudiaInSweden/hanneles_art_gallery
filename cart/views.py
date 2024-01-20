from django.shortcuts import render, redirect


def view_cart(request):

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):

    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)
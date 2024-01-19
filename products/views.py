from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

def all_products (request):

    products = Product.objects.all()
    query = None
    categories = None
    formats = None

    if request.GET:

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'format' in request.GET:
            formats = request.GET['format'].split(',')
            products = products.filter(format__in=formats)
            formats = Product.objects.filter(name__in=formats)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a keyword to search through the catalogue!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(technique__icontains=query) | Q(size__icontains=query) | Q(category__name__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_format': formats,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)

from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Post, Category


def post_list(request):
    
    posts = Post.objects.filter(status=1).order_by("-date_created")
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            posts = posts.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
    
    context = {
        'posts': posts,
        'category_selected': categories,
    }

    return render(request, 'academy/blog.html', context)


def post_detail(request, slug):
    q = Post.objects.filter(slug__iexact=slug)

    if q.exists():
        q = q.first()
    else:
        return HttpResponse('<h1>Post Not Found</h1>')

    context = {'post': q}
    return render(request, 'academy/post_detail.html', context)
    


# @login_required
# def add_product(request):
#     """ Add a new painting to the store """
#     if not request.user.is_superuser:
#         messages.error(request, 'You are not authorized to perform this task.')
#         return redirect(reverse('home'))

#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             product = form.save()
#             messages.success(request, 'The painting was added successfully!')
#             return redirect(reverse('product_detail', args=[product.id]))
#         else:
#             messages.error(request, 'Failed to add painting! Please ensure \
#                 that the form is valid!')
#     else:
#         form = ProductForm()
#     template = 'products/add_product.html'
#     context = {
#         'form': form,
#     }

#     return render(request, template, context)


# @login_required
# def edit_product(request, product_id):
#     """ Edit a painting """
#     if not request.user.is_superuser:
#         messages.error(request, 'You are not authorized to perform this task.')
#         return redirect(reverse('home'))

#     product = get_object_or_404(Product, pk=product_id)
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES, instance=product)
#         if form.is_valid():
#             form.save()
#             messages.info(request, 'The painting was updated successfully!')
#             return redirect(reverse('product_detail', args=[product.id]))
#         else:
#             messages.error(request, 'Failed to update painting! Please ensure \
#                 that the form is valid!')
#     else:
#         form = ProductForm(instance=product)
#         messages.info(request, f'You are editing painting "{product.name}"')

#     template = 'products/edit_product.html'
#     context = {
#         'form': form,
#         'product': product,
#     }

#     return render(request, template, context)


# @login_required
# def delete_product(request, product_id):
#     """ Delete a painting """
#     if not request.user.is_superuser:
#         messages.error(request, 'You are not authorized to perform this task.')
#         return redirect(reverse('home'))

#     product = get_object_or_404(Product, pk=product_id)
#     product.delete()
#     messages.info(request, 'The painting has been deleted!')
#     return redirect(reverse('products'))

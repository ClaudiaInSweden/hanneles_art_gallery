from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django import forms
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post, Category
from .forms import PostForm, AddPostForm


def post_list(request):
    posts = Post.objects.filter(status=1).order_by("-date_created")
    categories = Category.objects.all()
    current_category = None

    if request.GET:
        if 'category' in request.GET:
            current_category = request.GET['category'].split(',')
            posts = posts.filter(category__name__in=current_category)
            current_category = current_category[0]
            # categories = Category.objects.filter(name__in=categories)
    
    paginator = Paginator(posts, 3) # 2 posts in each page
    page = request.GET.get('page')
    try:
       posts = paginator.page(page)
    except PageNotAnInteger:
       # If page is not an integer deliver the first page
       posts = paginator.page(1)
    except EmptyPage:
       # If page is out of range deliver last page of results
       posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
        'page': page,
        'categories': categories,
        'current_category': current_category,
    }

    return render(request, 'academy/academy.html', context)



def post_detail(request, slug):
    post = Post.objects.filter(slug__iexact=slug)

    if post.exists():
        post = post.first()
    else:
        return redirect(reverse('academy'))

    context = {'post': post}
    return render(request, 'academy/post_detail.html', context)
    


@login_required
def create_post(request):
    """ Add a new post to the blog """
    if not request.user.is_superuser:
        messages.error(request, 'You are not authorized to perform this task.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        post_form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'The blog post has been added!')
            return redirect('academy')
        else:
            messages.error(request, 'Failed to create blog post! Please ensure \
                that the form is valid!')
            post_form = AddPostForm()

    template = 'academy/create_post.html'
    context = {
        'form': post_form,
    }

    return render(request, template, context)


@login_required
def update_post(request, slug):
    """ Update a post """
    if not request.user.is_superuser:
        messages.error(request, 'You are not authorized to perform this task.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.info(request, 'The post was updated successfully!')
            return redirect(reverse('academy'))
        else:
            messages.error(request, 'Failed to update post! Please ensure \
                that the form is valid!')
    else:
        form = PostForm(instance=post)

    template = 'academy/update_post.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


@login_required
def delete_post(request, slug):
    """ Delete a post """
    if not request.user.is_superuser:
        messages.error(request, 'You are not authorized to perform this task.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        post.delete()
        messages.info(request, 'The blog post has been deleted!')
        return redirect(('academy'))
    context = {'post': post}
    return render(request, 'academy/delete_post.html', context)

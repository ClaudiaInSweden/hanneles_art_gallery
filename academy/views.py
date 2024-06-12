from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post, Category


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

    return render(request, 'academy/blog.html', context)


def blog_admin(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
   
    paginator = Paginator(posts, 5) # 5 posts in each page
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
    }

    return render(request, 'academy/blog_admin.html', context)


def post_detail(request, slug):
    q = Post.objects.filter(slug__iexact=slug)

    if q.exists():
        q = q.first()
    else:
        return HttpResponse('<h1>Post Not Found</h1>')

    context = {'post': q}
    return render(request, 'academy/post_detail.html', context)
    


@login_required
def add_post(request):
    """ Add a new post to the blog """
    if not request.user.is_superuser:
        messages.error(request, 'You are not authorized to perform this task.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'The blog post has been created!')
            return redirect(reverse('post_detail', args=[post.slug]))
        else:
            messages.error(request, 'Failed to create blog post! Please ensure \
                that the form is valid!')
    else:
        form = PostForm()
    template = 'blog/add_post.html'
    context = {
        'form': form,
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
            return redirect(reverse('post_detail', args=[product.slug]))
        else:
            messages.error(request, 'Failed to update post! Please ensure \
                that the form is valid!')
    else:
        form = PostForm(instance=post)
        messages.info(request, f'You are editing the post with heading "{post.header}"')

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
    post.delete()
    messages.info(request, 'The blog post has been deleted!')
    return redirect(reverse('blog'))

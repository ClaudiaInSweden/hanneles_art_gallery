from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.db.models import Avg
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Review
from .forms import ReviewForm



def index(request):
    reviews = Review.objects.all()
    average_rating = Review.objects.all().aggregate(rating=Avg('rating'))
    
    context = {
    'reviews': reviews,
    'average_rating': average_rating,
    }

    return render(request, 'home/index.html', context)


def privacy_policy(request):

    return render(request, 'home/privacy_policy.html')



def reviews(request):

    # Getting all reviews
    reviews = Review.objects.all()
            
    # Getting average rating
    average_rating = Review.objects.all().aggregate(rating=Avg('rating'))

    new_review = None
    add_review = True
    """
    Check if user is logged in and has already submitted a Review
    If so, the form to submit a review will not be visible to this user.
    """
    if request.user.is_authenticated:
        user_review_count = Review.objects.filter(user=request.user).count()
        
        if user_review_count > 0:
            add_review = False
    """
    If user does not exist, user will be set to none 
    """
    try:
        user = User.objects.get(username=request.user)
    except User.DoesNotExist:
        user = None


    if request.method == 'POST':
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            """
            Form save will be committed first when user is assigned to review
            """
            new_review = review_form.save(commit=False)
            new_review.user = user
            new_review.save()

            messages.info(request, 'Thank you for your review!')
            return redirect(reverse('reviews'))
    else:
        review_form = ReviewForm()

    template_name = 'home/reviews.html'

    context = {
    'reviews': reviews,
    'average_rating': average_rating,
    'review_form': review_form,
    'add_review': add_review,
    }

    return render(request, template_name, context)


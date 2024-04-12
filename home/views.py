from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.db.models import Avg
from django.contrib import messages
from .models import Review
from .forms import ReviewForm
from profiles.models import UserProfile



def index(request):

    return render(request, 'home/index.html')


def privacy_policy(request):

    return render(request, 'home/privacy_policy.html')


# def reviews(request):

#     # Getting all reviews
#     reviews = Review.objects.all()

#     # Getting average rating
#     average_rating = Review.objects.all().aggregate(rating=Avg('rating'))

#     context = {
#     'reviews': reviews,
#     'average_rating': average_rating,
#     'review_form': review_form,
#     }

#     return render(request, 'home/reviews.html', context)


def reviews(request):

    # Getting all reviews
    reviews = Review.objects.all()
    user = UserProfile.objects.get(user=request.user)
    new_review = None

    # Getting average rating
    average_rating = Review.objects.all().aggregate(rating=Avg('rating'))

    if request.method == 'POST':
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
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
    }

    return render(request, template_name, context)


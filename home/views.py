from django.shortcuts import render
from .models import Review
from .forms import ReviewForm


def index(request):

    return render(request, 'home/index.html')


def privacy_policy(request):
    return render(request, 'home/privacy_policy.html')




def submit_review(request):
    """
    Check if there is aready a review from this user. If there is the review will be update.
    If there is no review, a new review will be created.
    """
    if request.method == 'POST':
        try:
            reviews = Review.objects.get(user_profile__id=request.user_profile.id)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(request, 'Thank you! Your review has been updated.')
            return redirect(reverse('home/index.html'))
        except Review.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = Review()
                data.rating = form.cleaned_data['rating']
                data.review_title = form.cleaned_data['review_title']
                data.review_body = form.cleaned_data['review_body']
                data.user_profile_id = request.user_profile.id
                data.save()
                messages.success(request, 'Thank you! Your review has been submitted.')
                return redirect(reverse('home/index.html'))


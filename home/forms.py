from django import forms
from .models import Review



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review 
        fields = ['show_name', 'rating', 'review_title', 'review_body']
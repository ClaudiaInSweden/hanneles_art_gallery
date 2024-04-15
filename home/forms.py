from django import forms
from .models import Review



class ReviewForm(forms.ModelForm):
    review_body = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Write your review here...', 'rows': 5}))
    
    class Meta:
        model = Review 
        fields = ['display_name', 'rating', 'review_title', 'review_body']
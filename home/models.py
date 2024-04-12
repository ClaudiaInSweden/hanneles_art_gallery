from django.db import models
from django.conf import settings
from datetime import datetime

from profiles.models import UserProfile



# Create your models here.
class Review(models.Model):

    RATING = (
        (1, "★☆☆☆☆"),
        (2, "★★☆☆☆"),
        (3, "★★★☆☆"),
        (4, "★★★★☆"),
        (5, "★★★★★"),
    )
   
    user = models.ForeignKey(UserProfile, default=None, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING, default=None)
    display_name = models.CharField(max_length=100, null=True, blank=True)
    review_title = models.CharField(max_length=100, null=True, blank=True)
    review_body = models.TextField(max_length=500, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering: ('-date_created')

    def __str__(self):
        return self.review_title

    def get_rating(self):
        return f'Rating: {self.rating} Review: {self.review_title}'

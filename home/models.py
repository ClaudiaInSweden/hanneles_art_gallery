from django.db import models
from django.conf import settings
from datetime import datetime
from django.contrib.auth.models import User
from profiles.models import UserProfile

# Create your models here.
class Review(models.Model):

    SHOW_NAME = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
 
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    show_name = models.CharField(max_length=5, choices=SHOW_NAME, default='Yes')
    rating = models.FloatField()
    review_title = models.CharField(max_length=100, null=True, blank=True)
    review_body = models.TextField(max_length=500, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

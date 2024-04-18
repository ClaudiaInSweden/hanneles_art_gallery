from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Review(models.Model):

    RATING = (
        (1, "★☆☆☆☆"),
        (2, "★★☆☆☆"),
        (3, "★★★☆☆"),
        (4, "★★★★☆"),
        (5, "★★★★★"),
    )

    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING, null=False, blank=False)
    display_name = models.CharField(max_length=100, null=True, blank=True)
    review_title = models.CharField(max_length=100, null=False, blank=False)
    review_body = models.TextField(max_length=500, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return f'Rating: {self.rating} Review: {self.review_title}'

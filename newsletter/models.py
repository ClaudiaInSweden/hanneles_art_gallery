from django.db import models

# Create your models here.
class Subscribers(models.Model):

    class Meta:
        verbose_name_plural = 'Subscribers'

    email = models.EmailField(null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class MailContent(models.Model):
    subject = models.CharField(max_length=254, null=False, blank=False)
    content = models.TextField(null=False, blank=False, default='\n \nUnsubscribe: https://hanneles-art-gallery-99fb21934da8.herokuapp.com/newsletter/unsubscribe/')

    def __str__(self):
        return self.subject

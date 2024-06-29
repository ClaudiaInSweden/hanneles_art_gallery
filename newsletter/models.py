from django.db import models

# Create your models here.
class Subscribers(models.Model):

    class Meta:
        verbose_name_plural = 'Subscribers'

    email = models.EmailField(null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class MailContent(models.Model):
    subject = models.CharField(max_length=254, null=True)
    content = models.TextField(null=True)

    def __str__(self):
        return self.subject

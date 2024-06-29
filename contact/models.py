from django.db import models

# Create your models here.
class Contact(models.Model):

    class Meta:
        verbose_name_plural = 'Contact forms'
        ordering = ['-date']

    TOPIC = (
        (1, 'Painting'),
        (2, 'Payment'),
        (3, 'Delivery'),
        (4, 'Other'),
    )

    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True)
    topic = models.IntegerField(choices=TOPIC, null=True, blank=True)
    message = models.TextField(max_length=500, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message {self.message} from {self.email} about {self.topic}'

from django.contrib import admin
from .models import Subscribers, MailContent

# Register your models here.
admin.site.register(Subscribers)
admin.site.register(MailContent)
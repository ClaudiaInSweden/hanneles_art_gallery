from django.contrib import admin
from .models import Contact

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_filter = ('topic', 'date')
    search_fields = ['name', 'email', 'message']
from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'topic', 'date')
    list_filter = ('topic', 'date')
    search_fields = ['name', 'email', 'message']

    ordering = ('-date',)

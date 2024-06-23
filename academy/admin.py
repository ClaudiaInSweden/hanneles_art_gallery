from django.contrib import admin
from .models import Post, Category, Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'date_added', 'active')
    list_filter = ('active', 'date_added')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
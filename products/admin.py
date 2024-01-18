from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sold',
        'name',
        'category',
        'size',
        'price',
        'image',
    )

    ordering = ('sold',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
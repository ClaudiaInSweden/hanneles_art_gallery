from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):

    FRAMED = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )

    FORMAT = (
        ('Portrait', 'Portrait'),
        ('Landscape', 'Landscape'),
        ('Square', 'Square')
    )

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    artist = models.CharField(max_length=254, default='Hannele K.')
    size = models.CharField(max_length=254)
    format = models.CharField(max_length=254, choices=FORMAT, default='Portrait')
    technique = models.CharField(max_length=254)
    framed = models.CharField(max_length=5, choices=FRAMED, default='No')
    sold = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name
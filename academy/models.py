from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from art_gallery.utils import slugify_instance_title
from ckeditor.fields import RichTextField


STATUS_CHOICES = ((0, "Draft"), (1, "Published"))


class Category(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Post(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    title = models.CharField(max_length=254)
    slug = models.SlugField(max_length=254, null=True, blank=True, unique=True)
    introtext = models.TextField()
    # bodytext = models.TextField()
    bodytext = RichTextField(blank=True, null=True)
    link = models.CharField(max_length=254, null=True, blank=True)
    blog_image = models.ImageField(upload_to='academy_images/', null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


def post_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        slugify_instance_title(instance, save=False)

pre_save.connect(post_pre_save, sender=Post)


def post_post_save(sender, instance, created, *args, **kwargs):
    if created:
        slugify_instance_title(instance, save=True)

post_save.connect(post_post_save, sender=Post)

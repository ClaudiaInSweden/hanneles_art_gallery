from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='blog'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('add_post/', views.add_post, name='add_post'),
    path('update_post/<slug:slug>/', views.update_post, name='update_post'),
    path('blog_admin', views.blog_admin, name='blog_admin'),
]
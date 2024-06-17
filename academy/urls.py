from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='academy'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('create_post/', views.create_post, name='create_post'),
    path('update_post/<slug:slug>/', views.update_post, name='update_post'),
    path('delete_post/<slug:slug>/', views.delete_post, name='delete_post'),
]
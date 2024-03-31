from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('submit_review/', views.submit_review, name='submit_review'),
    path('privacy/', views.privacy_policy, name='privacy_policy'),
]

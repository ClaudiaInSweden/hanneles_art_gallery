from django.urls import path
from . import views

urlpatterns = [
    path('subscribe/', views.subscribe, name='subscribe'),
    path('newsletter/', views.mail_content, name='mail_content')
]
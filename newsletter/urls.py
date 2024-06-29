from django.urls import path
from . import views

urlpatterns = [
    path('newsletter/subscribe/', views.subscribe, name='subscribe'),
    path('newsletter/mailcontent/', views.mail_content, name='mail_content')
]
from django.shortcuts import render
from .models import Subscribers, MailContent
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def subscribe(request):

    context = {

    }
    return render(request, 'newsletter/subscribe.html', context)


def mail_content(request):

    context = {

    }
    return render(request, 'newsletter/mailcontent.html', context)
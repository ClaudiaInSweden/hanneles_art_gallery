from django.shortcuts import render, redirect
from .models import Subscribers, MailContent
from .forms import SubscribeForm, MailContentForm
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'You have successfully subscribed to our newsletter!')
            return redirect('home')
    else:
        form = SubscribeForm()

    context = {
        'form': form,
    }
    return render(request, 'newsletter/subscribe.html', context)


def mail_content(request):
    if request.method == 'POST':
        form = MailContentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'The newsletter has been sent!')
            return redirect('home')
    else:
        form = MailContentForm()
    context = {
        'form': form
    }
    return render(request, 'newsletter/mailcontent.html', context)
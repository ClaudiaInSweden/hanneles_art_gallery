from django.shortcuts import render, redirect
from .models import Subscribers, MailContent
from .forms import SubscribeForm, MailContentForm
from django.contrib import messages
from django.core.mail import send_mail
from django_pandas.io import read_frame

# Create your views here.
def subscribe(request):
    form = SubscribeForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if Subscribers.objects.filter(email=instance.email).exists():
            messages.info(request, 'This email already exist!')
        else:
            instance.save()
            messages.info(request, 'You have successfully subscribed to our newsletter!')
            return redirect('home')

    context = {
        'form': form,
    }
    return render(request, 'newsletter/subscribe.html', context)


def unsubscribe(request):
    form = SubscribeForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if Subscribers.objects.filter(email=instance.email).exists():
            Subscribers.objects.filter(email=instance.email).delete()
            messages.info(request, 'You have successfully unsubscribed! Sorry to see you go!')
            return redirect('home')
        else:
            messages.info(request, 'Sorry, but your email address does not exist in our database!')
            return redirect('home')

    context = {
        'form': form,
    }
    return render(request, 'newsletter/unsubscribe.html', context)


def mail_content(request):
    """
    Create a variable to get all subscribers.
    Create a dataframe for email addresses of the subscribers.
    Retrieve values of the email addresses and transform them into a list
    """
    emails = Subscribers.objects.all()
    df = read_frame(emails, fieldnames=['email'])
    mail_list = df['email'].values.tolist()
    
    if request.method == 'POST':
        form = MailContentForm(request.POST)
        if form.is_valid():
            form.save()
            subject = form.cleaned_data.get('subject')
            content = form.cleaned_data.get('content')
            send_mail(
                subject,
                content,
                '',
                mail_list,
                fail_silently=False,
        )
            messages.info(request, 'The newsletter has been sent!')
            return redirect('home')
    else:
        form = MailContentForm()
    context = {
        'form': form
    }
    return render(request, 'newsletter/mailcontent.html', context)
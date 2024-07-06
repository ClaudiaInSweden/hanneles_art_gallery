from django.shortcuts import render, redirect, reverse
from .models import Subscribers, MailContent
from .forms import SubscribeForm, MailContentForm
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required


def subscribe(request):
    """
    If user enters an email address that already exists
    in database a message will be displayed. If the address
    does not yet exist, it is added to the database
    """
    form = SubscribeForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if Subscribers.objects.filter(email=instance.email).exists():
            messages.info(request, 'This email address already exists!')
        else:
            instance.save()
            messages.info(request, 'You have successfully subscribed \
                to our newsletter!')
            return redirect('home')

    context = {
        'form': form,
    }
    return render(request, 'newsletter/subscribe.html', context)


def unsubscribe(request):
    """
    If user enters an existing email address it is removed from the database.
    If the email address does not exist a message will be displayed.
    """
    form = SubscribeForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if Subscribers.objects.filter(email=instance.email).exists():
            Subscribers.objects.filter(email=instance.email).delete()
            messages.info(request, f'You have successfully unsubscribed!\
                 \nSorry, to see you go!')
            return redirect('home')
        else:
            messages.error(request, f'It seems the email address does not \
                exist in our database!\nPlease enter a valid email address.')
            return redirect('home')

    context = {
        'form': form,
    }
    return render(request, 'newsletter/unsubscribe.html', context)


@login_required
def mail_content(request):
    """
    Check if user is logged in as superuser. If not, display error message
    and redirect to start page
    """
    if not request.user.is_superuser:
        messages.error(request, 'You are not authorized to perform this task.')
        return redirect(reverse('home'))

    emails = Subscribers.objects.values_list("email", flat=True)

    """
    Send email with newsletter subject and content to subsribers.
    Use sender email as saved in settings, use to field with
    default sender email as saved in settings.
    The actual subscriber email addresses will be added to bcc
    to avoid exposure to other subscribers.
    """
    if request.method == 'POST':
        form = MailContentForm(request.POST)
        if form.is_valid():
            form.save()
            subject = form.cleaned_data.get('subject')
            content = form.cleaned_data.get('content')
            send_from = settings.DEFAULT_FROM_EMAIL
            send_to = settings.DEFAULT_FROM_EMAIL
            bcc_list = list(emails)

            email = EmailMessage(
                subject,
                content,
                send_from,
                (send_to,),
                bcc=bcc_list,
            )
            email.send(fail_silently=False)
            messages.info(request, 'The newsletter has been sent!')
            return redirect('home')
    else:
        form = MailContentForm()
    context = {
        'form': form
    }
    return render(request, 'newsletter/mailcontent.html', context)

from django import forms
from .models import Subscribers, MailContent


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = ('email',)


class MailContentForm(forms.ModelForm):
    class Meta:
        model = MailContent
        fields = '__all__'
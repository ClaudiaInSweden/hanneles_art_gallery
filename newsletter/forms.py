from django import forms
from .models import Subscribers, MailContent


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = ('email',)

        def clean_email(self):
            email = self.cleaned_data.get('email')

            return email


class MailContentForm(forms.ModelForm):
    class Meta:
        model = MailContent
        fields = '__all__'
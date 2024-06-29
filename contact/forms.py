from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'topic', 'message',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'aria-label': 'Your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'aria-label': 'E-Mail'}),
            'topic': forms.Select(attrs={'class': 'form-control',
                                         'aria-label': 'Topic'}),
            'message': forms.Textarea(attrs={'class': 'form-control',
                                             'aria-label': 'Message',
                                             'rows': 8,}),
        }

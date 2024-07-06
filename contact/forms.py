from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'topic', 'message',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'aria-label': 'Your name',
                                           'placeholder': 'Your name *'}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'aria-label': 'E-Mail',
                                             'placeholder': 'E-Mail *'}),
            'topic': forms.Select(attrs={'class': 'form-control',
                                         'aria-label': 'Topic'}),
            'message': forms.Textarea(attrs={'class': 'form-control',
                                             'aria-label': 'Message',
                                             'rows': 8,
                                             'placeholder': 'Your message'}),
        }

    def __init__(self, *args, **kwargs):
        """
        Set autofocus on name field and remove auto-labels
        """
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].label = False

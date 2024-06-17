from django import forms
from .widgets import CustomClearableFileInput
from .models import Post, Category


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('header', 'category', 'introtext', 'bodytext', 'link', 'blog_image', 'image_url', 'status',)

        widgets = {
            'header': forms.TextInput(attrs={'class': 'form-control',
                                             'aria-label': 'Header'}),
            'category': forms.Select(attrs={'class': 'form-control',
                                            'aria-label': 'Category'}),
            'introtext': forms.Textarea(attrs={'class': 'form-control',
                                               'aria-label': 'Introtext',
                                               'rows': 5,}),
            'bodytext': forms.Textarea(attrs={'class': 'form-control',
                                              'aria-label': 'Bodytext',}),
            'link': forms.URLInput(attrs={'class': 'form-control',
                                          'aria-label': 'URL Input'}),     
            'status': forms.Select(attrs={'class': 'form-control',
                                          'aria-label': 'Status'}),
            'image_url': forms.URLInput(attrs={'class': 'form-control',
                                               'aria-label': 'Image URL Input'}),
        }
        blog_image = forms.ImageField(label='Image',
                                      widget=CustomClearableFileInput)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_name = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_name
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class AddPostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ('id', 'slug', 'date_created')

        widgets = {
            'header': forms.TextInput(attrs={'class': 'form-control',
                                             'aria-label': 'Header'}),
            'category': forms.Select(attrs={'class': 'form-control',
                                            'aria-label': 'Category'}),
            'introtext': forms.Textarea(attrs={'class': 'form-control',
                                               'aria-label': 'Introtext',
                                               'rows': 5,}),
            'bodytext': forms.Textarea(attrs={'class': 'form-control',
                                              'aria-label': 'Bodytext',}),
            'link': forms.URLInput(attrs={'class': 'form-control',
                                          'aria-label': 'URL Input'}),     
            'status': forms.Select(attrs={'class': 'form-control',
                                          'aria-label': 'Status'}),
            'image_url': forms.URLInput(attrs={'class': 'form-control',
                                               'aria-label': 'Image URL Input'}),
        }
        blog_image = forms.ImageField(label='Image',
                                      widget=CustomClearableFileInput)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_name = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_name
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

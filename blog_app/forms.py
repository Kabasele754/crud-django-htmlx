from django import forms

from .models import Blog


class BlogForm(forms.ModelForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = Blog
        fields = ['title','image', 'description']

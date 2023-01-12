from django import forms
from blog.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'status']


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=50, required=False, label='Search')

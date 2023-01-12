from django import forms
from blog.models import Post
from django.forms import widgets


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'status', 'category']
        widgets = {'category': widgets.CheckboxSelectMultiple}


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=50, required=False, label='Search')

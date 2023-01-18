from django import forms
from blog.models import Post, Comment
from django.forms import widgets


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'status', 'category']
        widgets = {'category': widgets.CheckboxSelectMultiple}


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=50, required=False, label='Search')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

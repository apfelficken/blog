from django.shortcuts import get_object_or_404, redirect, reverse
from django.views.generic import DetailView
from django.utils.http import urlencode
from blog.forms import SimpleSearchForm
from blog.models import Post, Category
from django.db.models import Q
from django.views.generic.list import MultipleObjectMixin


class CategoryPostView(DetailView, MultipleObjectMixin):
    template_name = 'category/category_index.html'
    model = Category
    paginate_by = 3

    def get_context_data(self, **kwargs):
        object_list = Post.objects.filter(category=self.get_object())
        context = super(CategoryPostView, self).get_context_data(object_list=object_list, **kwargs)
        return context

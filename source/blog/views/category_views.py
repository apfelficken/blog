from django.views.generic import DetailView
from django.views.generic.list import MultipleObjectMixin
from blog.models import Post, Category


class CategoryPostView(DetailView, MultipleObjectMixin):
    template_name = 'category/category_index.html'
    model = Category
    paginate_by = 3

    def get_context_data(self, **kwargs):
        object_list = Post.objects.filter(category=self.get_object())
        context = super(CategoryPostView, self).get_context_data(object_list=object_list, **kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        return context

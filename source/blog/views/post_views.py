from django.shortcuts import get_object_or_404, redirect, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from django.utils.http import urlencode
from blog.forms import PostForm, SimpleSearchForm
from blog.models import Post, Category
from django.db.models import Q


class PostIndexView(ListView):
    template_name = 'post/post_index.html'
    context_object_name = 'posts'
    model = Post
    paginate_by = 3
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(Q(title__icontains=self.search_value) |
                                       Q(body__icontains=self.search_value))
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        categories = Category.objects.all()
        context['categories'] = categories
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search'] = self.search_value
        return context


class PostView(DetailView):
    template_name = 'post/post_view.html'
    model = Post
    context_object_name = 'post'


class PostAddView(CreateView):
    template_name = 'post/post_add.html'
    model = Post
    form_class = PostForm
    context_object_name = 'post'

    def form_valid(self, form):
        user = self.request.user.pk
        self.object = Post.objects.create(**form.cleaned_data)
        self.object.user = user
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.object.slug, 'pk': self.object.pk})


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post/post_update.html'
    form_class = PostForm
    context_object_name = 'post'

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.object.slug, 'pk': self.object.pk})


class PostDeleteView(View):
    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return redirect('blog:index')

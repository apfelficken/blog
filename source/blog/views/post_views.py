from django.shortcuts import get_object_or_404, redirect, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View

from blog.forms import PostForm
from blog.models import Post


class PostIndexView(ListView):
    template_name = 'post/post_index.html'
    context_object_name = 'posts'
    model = Post
    paginate_by = 3
    paginate_orphans = 1


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

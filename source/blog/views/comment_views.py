from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView

from blog.forms import CommentForm
from blog.models import Comment, Post


class PostCommentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'comment/add_comment.html'
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.object.post.slug, 'pk': self.object.post.pk})

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentUpdateView(PermissionRequiredMixin, UpdateView):
    model = Comment
    template_name = 'comment/update_comment.html'
    form_class = CommentForm
    context_object_name = 'comment'
    permission_required = 'blog.change_comment'

    def has_permission(self):
        return self.request.user.has_perm('webapp.change_comment') or self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.object.post.slug, 'pk': self.object.post.pk})


class CommentDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'blog.delete_comment'
    model = Comment

    def has_permission(self):
        comment = get_object_or_404(Comment, pk=self.kwargs.get('pk'))
        return super().has_permission() or comment.author == self.request.user

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.object.post.slug, 'pk': self.object.post.pk})

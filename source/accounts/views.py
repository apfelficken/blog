from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView
from django.views.generic.list import MultipleObjectMixin
from accounts.models import Profile
from blog.models import Post
from accounts.forms import MyUserCreationForm
from django.contrib.auth.models import User


class RegisterView(CreateView):
    model = User
    form_class = MyUserCreationForm
    template_name = 'registration.html'

    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(user=user)
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url

        next_url = self.request.POST.get('next')
        if next_url:
            return next_url

        return reverse('blog:index')


class UserDetailView(LoginRequiredMixin, DetailView, MultipleObjectMixin):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'
    paginate_by = 3
    slug_field = 'username'

    def get_context_data(self, **kwargs):
        object_list = Post.objects.filter(author=self.get_object())
        return super().get_context_data(object_list=object_list, **kwargs)

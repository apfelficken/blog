from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from slugify import slugify


# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Name', unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Title')
    slug = models.SlugField(default='', editable=False, max_length=200, null=False)
    author = models.ForeignKey(User, related_name='posts', on_delete=models.SET_DEFAULT, default=1,
                               verbose_name="Author")
    body = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Content")
    publish = models.DateTimeField(default=timezone.now, verbose_name='Publish date')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    status = models.ForeignKey('blog.Status', to_field='name', default='Draft', related_name='status',
                               on_delete=models.PROTECT, verbose_name='Status')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={
            'pk': self.id,
            'slug': self.slug,
        })

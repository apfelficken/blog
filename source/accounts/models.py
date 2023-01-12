from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from slugify import slugify


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), related_name='profile', on_delete=models.CASCADE,
                                verbose_name='User')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Birth date')
    avatar = models.ImageField(null=True, blank=True, upload_to='user_avatar', verbose_name='Avatar')
    github = models.URLField(null=True, blank=True, verbose_name='GitHub')
    bio = models.TextField(null=True, blank=True, verbose_name='Bio')
    slug = models.SlugField(default='', editable=False, max_length=200, null=False, unique=True)

    def __str__(self):
        return f"{self.user.username} 's Profile"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        return super(Profile, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("accounts:detail", kwargs={
            'id': self.user.pk,
        })

    class Meta:
        db_table = 'profile'
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

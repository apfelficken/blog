from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), related_name='profile', on_delete=models.CASCADE,
                                verbose_name='User')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Birth date')
    avatar = models.ImageField(null=True, blank=True, upload_to='user_avatar', verbose_name='Avatar')
    github = models.URLField(null=True, blank=True, verbose_name='GitHub')
    bio = models.TextField(null=True, blank=True, verbose_name='Bio')

    def __str__(self):
        return f"{self.user.username} 's Profile"

    def get_absolute_url(self):
        return reverse("accounts:detail", kwargs={
            'username': self.user.username,
        })

    class Meta:
        db_table = 'profile'
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

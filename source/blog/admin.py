from django.contrib import admin
from .models import Post, Status, Category

# Register your models here.
admin.site.register(Post)
admin.site.register(Status)
admin.site.register(Category)

# Generated by Django 4.1.5 on 2023-01-12 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_category_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='', editable=False, max_length=200, unique=True),
        ),
    ]

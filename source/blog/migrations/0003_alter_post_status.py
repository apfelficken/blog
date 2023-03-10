# Generated by Django 4.1.5 on 2023-01-10 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_status_alter_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.ForeignKey(default='Draft', on_delete=django.db.models.deletion.PROTECT, related_name='status', to='blog.status', to_field='name', verbose_name='Status'),
        ),
    ]

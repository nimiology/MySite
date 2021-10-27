# Generated by Django 3.2.8 on 2021-10-24 15:21

import Blog.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('github', models.URLField()),
                ('thumbnail1', models.ImageField(default='', upload_to=Blog.utils.upload_project_picture)),
                ('thumbnail2', models.ImageField(default='', upload_to=Blog.utils.upload_project_picture)),
                ('thumbnail3', models.ImageField(default='', upload_to=Blog.utils.upload_project_picture)),
                ('text', models.TextField()),
                ('publishDate', models.DateTimeField(auto_now_add=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('publish', models.BooleanField()),
            ],
        ),
    ]
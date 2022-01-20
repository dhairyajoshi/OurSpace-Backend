# Generated by Django 4.0.1 on 2022-01-20 16:19

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_newuser_likes_newuser_posts'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='bio',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='newuser',
            name='cfp',
            field=models.ImageField(default='cfps/default.jpg', upload_to=accounts.models.upload_to_cfp, verbose_name='Image'),
        ),
    ]
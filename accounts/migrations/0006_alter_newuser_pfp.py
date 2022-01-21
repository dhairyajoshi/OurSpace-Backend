# Generated by Django 4.0.1 on 2022-01-21 18:57

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_newuser_bio_newuser_cfp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='pfp',
            field=models.ImageField(default='pfps/default.svg', upload_to=accounts.models.upload_to_pfp, verbose_name='Image'),
        ),
    ]

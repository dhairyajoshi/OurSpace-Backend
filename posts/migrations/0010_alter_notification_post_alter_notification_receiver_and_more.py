# Generated by Django 4.0.1 on 2022-01-18 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_alter_post_caption_alter_post_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='post',
            field=models.CharField(default='none', max_length=150),
        ),
        migrations.AlterField(
            model_name='notification',
            name='receiver',
            field=models.CharField(default='none', max_length=150),
        ),
        migrations.AlterField(
            model_name='notification',
            name='sender',
            field=models.CharField(default='none', max_length=150),
        ),
    ]
# Generated by Django 4.0.1 on 2022-01-17 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_remove_post_content_post_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=150)),
                ('receiver', models.CharField(max_length=150)),
                ('post', models.CharField(max_length=150)),
            ],
        ),
    ]

from django.contrib import admin
from .models import Notification, Post
# Register your models here.


admin.site.register(Post)
admin.site.register(Notification)

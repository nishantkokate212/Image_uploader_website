from django.contrib import admin
from .models import Posts
# Register your models here.
class PostsAdmin(admin.ModelAdmin):
    list_display=['user','caption','coverphoto']
admin.site.register(Posts)

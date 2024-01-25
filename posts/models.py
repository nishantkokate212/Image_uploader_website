from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User

# Create your models here.
class Posts(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    caption=models.CharField(max_length=150,null=True)
    photo=models.ImageField(upload_to='images/')

    def coverphoto(self):
        return mark_safe(f"<img src='{self.photo.url}' width='200'>")

    def __str__(self):
        return self.caption
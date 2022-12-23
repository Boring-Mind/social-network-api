from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)


class Like(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE, related_name="person")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post")
    created = models.DateTimeField(auto_now_add=True)

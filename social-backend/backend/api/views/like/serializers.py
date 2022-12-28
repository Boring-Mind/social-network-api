from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Post, Like


class LikeSerializer(serializers.ModelSerializer):
    person = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Like
        fields = ("id", "person", "post", "created")

from typing import Any, Dict

from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.cache import cache
from rest_framework import serializers

from api.models import Post, Like
from backend.middlewares import UpdateLastActivityMiddleware


class UserSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "last_login",
            "date_joined",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "password": {"write_only": True, "validators": [validate_password]},
            "email": {"required": True},
            "last_login": {"read_only": True},
            "date_joined": {"read_only": True},
        }

    def get_username(self, obj: User):
        return obj.email

    def create(self, validated_data: Dict[str, Any]) -> User:
        user = User.objects.create(
            username=validated_data["email"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user


class PostSerializer(serializers.ModelSerializer):
    """Post serializer.

    Write to Post can be performed only using authenticated user.
    """

    # author field is being propagated from the request
    # (currently authenticated user)
    author = serializers.PrimaryKeyRelatedField(read_only=True, required=False)

    class Meta:
        model = Post
        fields = ("author", "content", "created_on", "edited_on")
        read_only_fields = ["created_on", "edited_on"]

    def create(self, validated_data):
        # Request is passed to serializer's context from class-based view by default
        validated_data["author"] = self.context["request"].user

        return Post.objects.create(**validated_data)


class UserActivitySerializer(serializers.ModelSerializer):
    last_activity = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("id", "last_activity", "last_login")

    def get_last_activity(self, obj: User):
        return cache.get(
            UpdateLastActivityMiddleware.LAST_ACTIVITY_CACHE_TEMPLATE.format(
                user_id=obj.id
            )
        )


class LikeSerializer(serializers.ModelSerializer):
    person = serializers.PrimaryKeyRelatedField(read_only=True, required=False)
    post = serializers.PrimaryKeyRelatedField(read_only=True, required=False)

    class Meta:
        model = Like
        fields = ("id", "person", "post", "created")


class PostWithLikesSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    likes = LikeSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ("id", "author", "content", "created_on", "edited_on", "likes")

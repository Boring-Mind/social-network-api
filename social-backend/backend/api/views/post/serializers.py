from rest_framework import serializers

from api.models import Post
from api.views.like.serializers import LikeSerializer


class PostCreateSerializer(serializers.ModelSerializer):
    """Post create serializer.

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


class PostWithLikesSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    likes = LikeSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ("id", "author", "content", "created_on", "edited_on", "likes")

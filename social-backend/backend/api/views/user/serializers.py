from typing import Dict, Any

from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers


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

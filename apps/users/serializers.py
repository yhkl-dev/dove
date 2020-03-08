from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    user serializer class
    """
    username = serializers.CharField(required=False, read_only=False, max_length=32, lable="user name",
                                     help_text="user name")
    name = serializers.CharField(required=False, read_only=False, label="")

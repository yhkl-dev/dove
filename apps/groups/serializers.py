from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers

User = get_user_model()


class GroupSerializer(serializers.ModelSerializer):
    """
    group serializer class

    """

    def to_representation(self, instance):
        member = instance.user_set.count()
        ret = super(GroupSerializer, self).to_representation(instance)
        ret["member"] = member
        return ret

    class Meta:
        model = Group
        fields = ("id", "name")


class UserGroupSerializer(serializers.ModelSerializer):
    """
    user's group serializer class
    """

    groups = GroupSerializer(many=True)

    def to_representation(self, instance):
        name = instance.name
        ret = super(UserGroupSerializer, self).to_representation(instance)
        ret['name'] = name
        return ret

    class Meta:
        model = User
        fields = ("id", "username", "groups")

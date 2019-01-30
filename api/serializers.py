from django.contrib.auth.models import User, Group
from shop.models import mem
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class MemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = mem
        fields = ('url', 'author', 'disctiption', 'mem_img','cost','id')

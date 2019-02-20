from django.contrib.auth.models import User, Group
from shop.models import mem
from profiles.models import UserProfile
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
    author=serializers.StringRelatedField(many=False)
    class Meta:
        model = mem
        fields = ('url', 'author', 'disctiption', 'mem_img','cost','id')
class AddMemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=mem
        fields= ('disctiption', 'cost','available') #'mem_img',




class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user=UserSerializer()
    mems_of_profile= serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='mem-detail'
    )
    class Meta:
        model = UserProfile
        fields = ('url','user', 'user_balance', 'user_picture','mems_of_profile')

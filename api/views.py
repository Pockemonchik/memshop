from django.shortcuts import render
from django.contrib.auth.models import User, Group
from shop.models import mem
from rest_framework.decorators import action,permission_classes
from profiles.models import UserProfile
from rest_framework import serializers
from django.shortcuts import get_object_or_404
from rest_framework import viewsets,status
from .serializers import UserSerializer,AddMemSerializer,GroupSerializer,MemSerializer,ProfileSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated,AllowAny

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class MemViewSet(viewsets.ModelViewSet):

    queryset = mem.objects.filter(available=True)
    serializer_class = MemSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class  = ProfileSerializer
    serializer_action_classes = {
               'add_mem': AddMemSerializer,
               }
    # permission_classes=(AllowAny)
    @action(detail=True,methods=['post'])
    def add_mem(self, request, pk=None):
        profile=get_object_or_404(UserProfile,user__username="grisha")
        if request.method == 'POST':
            serializer=AddMemSerializer(data=request.data,context={'request': request})
            if serializer.is_valid():
                serializer.save(author=profile)
                return Response(serializer.data)
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)

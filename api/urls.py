from rest_framework import routers
from api import views
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.conf import settings
# Import static if not imported
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from rest_framework.authtoken import views as v

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'shopApi', views.MemViewSet)
router.register(r'profiles', views.ProfileViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
    path('api-token-auth/', v.obtain_auth_token, name='api-token-auth')
]

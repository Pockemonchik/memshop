from rest_framework import routers
from api import views
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.conf import settings
# Import static if not imported
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'shopApi', views.MemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

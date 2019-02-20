"""memdiller URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, url
    2. Add a URL to urlpatterns:  url('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.conf import settings
# Import static if not imported
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
urlpatterns = [
    url('admin/', admin.site.urls),
    url('auth/', include('django.contrib.auth.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^profiles/', include('profiles.urls')),
    url('shop/', include('shop.urls',namespace='shop')),
    url(r'^$', include('home.urls')),
    url('api/', include('api.urls')),
    url(r'^cart/', include('cart.urls',namespace='cart'))

]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL,
    document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

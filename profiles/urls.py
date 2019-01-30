from django.conf.urls import url
from . import views
from profiles.models import UserProfile
from django.conf import settings
from django.conf.urls.static import static

urlpatterns= [
    url(r'^(?P<slug>[\w-]+)/$',views.detail_profile, name='detail_profile'),
    ]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL,
    document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf.urls import url
from . import views
from profiles.models import UserProfile
from django.conf import settings
from django.conf.urls.static import static

urlpatterns= [
    url(r'^(?P<slug>[\w-]+)/$',views.detail_profile, name='detail_profile'),
    url(r'^add_to_shop/(?P<mem_id>\d+)/$',views.add_to_shop, name='add_to_shop'),
    url(r'^del_from_shop/(?P<mem_id>\d+)/$',views.del_from_shop, name='del_from_shop')
    ]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL,
    document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

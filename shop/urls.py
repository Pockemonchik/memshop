from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from shop.models import mem
from django.conf import settings
app_name = 'shop'
urlpatterns= [
    url('(?P<category_slug>[-\w]+)/',views.List_shop, name='List_shop_by_category'),
    url(r'^$',views.List_shop, name='List_shop'),
    url(r'^like', views.like, name='like'),

    # url(r'search/',views.search, name='search'),
    ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

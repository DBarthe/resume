from django.conf.urls import url

from .views import Index, Sitemap

urlpatterns = [
  url(r'^$', Index.as_view(), name='index'),
  url(r'^sitemap\.xml$', Sitemap.as_view(), name='sitemap'),
]
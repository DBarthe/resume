"""resume URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, i18n
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.views.static import serve

from . import settings
from website import urls as website_urls

urlpatterns = [
  url(r'^i18n/', include(i18n)),
]

urlpatterns += i18n_patterns(
  url(r'^admin/', include(admin.site.urls)),
  url(r'^', include(website_urls)),
)

if settings.DEBUG:
  urlpatterns += [
    url(r'^media/(?P<path>.*)$', serve, {
      'document_root': settings.MEDIA_ROOT,
    }),
  ]
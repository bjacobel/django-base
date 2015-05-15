from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from djangobase.apps.api import urls as api_urls
from djangobase.apps.core import urls as core_urls


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v{}/'.format(settings.API_VERSION), include(api_urls)),
    url(r'^', include(core_urls))
]

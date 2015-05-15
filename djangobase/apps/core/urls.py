from django.conf.urls import url
from djangobase.apps.core import views

urlpatterns = [
    url(r'^$', views.DefaultView, name="default"),
]
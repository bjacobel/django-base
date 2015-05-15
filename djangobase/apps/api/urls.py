from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .endpoints.root import api_root

router = DefaultRouter()

# routes for every model's create, retrieve, update, delete api endpoints

urlpatterns = [
    url(r'^$', api_root),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
from django.conf.urls import url, re_path
from . import views

urlpatterns = [
    url(r'^$', views.json_endpoint, name = 'json response')
]

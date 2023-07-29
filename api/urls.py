from django.urls import path

from . import views

urlpatterns = [path("", views.json_endpoint, name="json response")]

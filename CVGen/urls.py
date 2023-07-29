from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("Webapp.urls")),
    path("api/", include("API.urls")),
    path("admin/", admin.site.urls),
]

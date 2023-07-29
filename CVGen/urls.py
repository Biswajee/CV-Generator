from django.urls import include, path

urlpatterns = [
    path("", include("Webapp.urls")),
    path("api", include("API.urls")),
]

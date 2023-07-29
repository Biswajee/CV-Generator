from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup", views.signup, name="signup"),
    path("signup_creds", views.signupinfo, name="signup credentials"),
    path("signin", views.signin, name="signin"),
    path("verify", views.verify, name="signin verification"),
    path("form", views.formfill, name="formfillup"),
    path("logout", views.logout, name="logout"),
    path("profile/", views.profile, name="profile viewer"),
    path("read-docs", views.read_docs, name="Developer guide"),
    path("resume", views.form_submit, name="Resume display"),
]

from django.conf.urls import url, re_path
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'signup/$', views.signup, name = 'signup'),
    url(r'signup_creds/$', views.signupinfo, name = 'signup credentials'),
    url(r'signin/$', views.signin, name = 'signin'),
    url(r'verify/$', views.verify, name = 'signin verification'),
    url(r'form/$', views.formfill, name = 'formfillup'),
    url(r'logout/$', views.logout, name = 'logout'),
    url('profile/', views.profile, name = 'profile viewer'),
    url(r'read-docs/$', views.read_docs, name = 'Developer guide'),
    url(r'resume/$', views.form_submit, name = 'Resume display')
]

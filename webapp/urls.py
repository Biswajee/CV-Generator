from django.conf.urls import url, re_path
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'signup/$', views.signup, name = 'signup'),
    url(r'signin/$', views.signin, name = 'signin'),
    url('form/', views.formfill, name = 'formfillup'),
    url('profile/', views.profile, name = 'profile viewer'),
    url(r'read-docs/$', views.read_docs, name = 'Developer guide'),
    url(r'^submit/$', views.form_submit, name = 'Resume display')
]

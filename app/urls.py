from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^jobs/', views.jobs, name='index'),
    url(r'^candidates/', views.candidates, name='index'),
    url(r'^login/', views.login, name="login"),
    url(r'^filter/', views.filter, name="filter"),
    url(r'^signup/', views.signup, name="signup"),
    url(r'^category/', views.category, name="category"),
    url(r'^user_details1/', views.user_details1, name="category"),
    url(r'^loginForm/', views.candidates, name="login"),
    url(r'^location/', views.location, name="login"),
    url(r'^(?P<job_id>[0-9]+)/$', views.jobview, name='index'),
    url(r'^jobs/(?P<job_id>[0-9]+)/$', views.jobview, name='index'),
]
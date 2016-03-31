from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views
admin.autodiscover()

urlpatterns = [
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^loginurl/$', views.login, name="login_view"),
    url(r'^logouturl/$', views.logout_view, name='logout_view'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^$', views.home, name='home'),
]

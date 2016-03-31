from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views
admin.autodiscover()

urlpatterns = [
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', views.home, name='home'),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout_view, name='logout_view'),

]

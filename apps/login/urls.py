from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
   url(r'^$', 'login.views.home', name='home'),
   url(r'^admin/', include(admin.site.urls)),
]

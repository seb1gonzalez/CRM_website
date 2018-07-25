from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', views.homepage),
    url(r'^our_team/$',views.ourTeam),
    url(r'^services/$', views.services),
    url(r'^contact/$',views.contact)
]
urlpatterns+= staticfiles_urlpatterns()
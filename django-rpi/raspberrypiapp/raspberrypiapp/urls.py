from django.conf.urls import url
from django.contrib.auth.views import login
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', views.homepage),


]
urlpatterns+= staticfiles_urlpatterns()
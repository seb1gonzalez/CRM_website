from django.conf.urls import url
from django.contrib.auth.views import login
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', views.homepage),
    url(r'^login/$', views.login_view,name=login),

]
urlpatterns+= staticfiles_urlpatterns()
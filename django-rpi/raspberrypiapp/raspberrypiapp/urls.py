from django.conf.urls import url, include
from django.contrib.auth.views import login
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', views.homepage),
    url(r'^login/$', TemplateView.as_view(template_name="pages/login.html")),

]
urlpatterns+= staticfiles_urlpatterns()
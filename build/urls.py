from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.view_buildSelect),
    url(r'^(?P<prof>[\w\-]+)/$', views.view_build),
]
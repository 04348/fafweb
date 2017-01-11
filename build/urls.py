from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.view_buildSelect),
    url(r'^create/$', views.view_buildCreate),
    url(r'^_(?P<prof>[\w\-]+)/$', views.view_build),
]
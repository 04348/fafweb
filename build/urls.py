from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.view_buildSelect),
    url(r'^create/$', views.view_buildCreate, name="bcreate"),
    url(r'^_(?P<prof>[\w\-]+)/$', views.view_build),
    url(r'^_(?P<prof>[\w\-]+)/(?P<n>[1-9])/$', views.view_build_n),
]
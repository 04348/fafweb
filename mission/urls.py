from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.view_missionSelect),
    url(r'^(?P<mission>[\w\-]+)/$', views.view_mission),
]
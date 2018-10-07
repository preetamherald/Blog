from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^details/(?P<id>\d+)/$', views.details, name='details'),
    url(r'^', views.main, name='main'),
]

from django.conf.urls import url
from .views import *

app_name = 'post'

urlpatterns = [
    url(r'^index/$', postIndex, name = 'index'),
    url(r'^(?P<id>\d+)/$', postDetail, name ='detail'),
    url(r'^create/$', postCreate, name = 'create'),
    url(r'^(?P<id>\d+)/update/$', postUpdate, name = 'update'),
    url(r'^(?P<id>\d+)/delete/$', postDelete, name = 'delete'),

]

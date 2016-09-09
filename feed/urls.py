from django.conf.urls import url
from django.contrib import admin

from feed import views

urlpatterns = [
    url(r'^$', views.event_list, name='list'),
    url(r'^create/$', views.event_create),
    url(r'^(?P<id>\d+)/$', views.event_description, name='event_description'),
    url(r'^(?P<id>\d+)/edit/$', views.event_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', views.event_delete),
 ]

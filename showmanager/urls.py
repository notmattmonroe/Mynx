from django.conf.urls import *
from django.views.generic import ListView
from . import views

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.show_detail.as_view(), name='DetailView'),
    #url(r'^(?P<id>\d+)/$', views.show_detail),
    url(r'^$', views.index.as_view(), name='index'),
]
"""
urlpatterns = patterns('',
    #(r'^performers/(?P<id>\d+)/$', 'luke.showmanager.views.performer_detail'),
    #(r'^performers/$', 'luke.showmanager.views.performer_list'),
    (r'^(?P<id>\d+)/$', 'showmanager.views.show_detail'),
    (r'^$', ListView.as_view(model=show,)),
        url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
)
"""

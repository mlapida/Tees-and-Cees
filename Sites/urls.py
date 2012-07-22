from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from Sites.models import App

urlpatterns = patterns('',
	url(r'^$','Sites.views.list'),
	url(r'^(?P<slug>\w+)/$','Sites.views.appdetail'),
)
from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from Sites.models import App

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=App.objects.order_by('-pub_date')[:5],
            context_object_name='latest_apps_list',
            template_name='apps/index.html')),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=App,
            template_name='apps/detail.html'
            )),
)
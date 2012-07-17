from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'Sites.views.index'),
    url(r'^apps/', include('Sites.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^search/', include('haystack.urls')),
)
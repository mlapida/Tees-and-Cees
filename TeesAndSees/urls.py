from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'Sites.views.index'),
	#url(r'^$', include('haystack.urls')),
    url(r'^apps/', include('Sites.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', 'Sites.views.search'),
)


from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from Sites.models import Page, App
from haystack.query import SearchQuerySet
from haystack.views import search_view_factory, SearchView

#The home page view
def index(request):
    homepage_list = Page.objects.filter(Dest='home').order_by('-pub_date')[:5]
    c = Context({
        'homepage_list': homepage_list,
    })
    return render_to_response('apps/home.html', c, context_instance=RequestContext(request))
 
#the search page view    
def search(request):
    sqs = SearchQuerySet().all()
    homepage_list = Page.objects.filter(Dest='home').order_by('-pub_date')[:5]
    
    extra_context = Context({
        'homepage_list': homepage_list,
    })
    
    view = search_view_factory(
        view_class=SearchView,
        template='search/search.html',
        context_class=RequestContext,
        searchqueryset=sqs,
        )
    return view(request)	

#app detail page    
def appdetail(request, slug):
    appquery = get_object_or_404(App, slug=slug)
    c = Context({
        'app': appquery,
    })
    return render_to_response('apps/detail.html', c, context_instance=RequestContext(request))

#ugly list view    
def list(request):
    latest_apps_list = App.objects.order_by('-pub_date')[:5]
    c = Context({
        'latest_apps_list': latest_apps_list,
    })
    return render_to_response('apps/index.html', c, context_instance=RequestContext(request))
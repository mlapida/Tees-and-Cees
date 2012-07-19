# Create your views here.
from django.template import Context, loader
from Sites.models import Page
from django.http import HttpResponse
from haystack.query import SearchQuerySet
from haystack.views import search_view_factory
from haystack.views import SearchView

def index(request):
    homepage_list = Page.objects.filter(Dest='home').order_by('-pub_date')[:5]
    t = loader.get_template('apps/home.html')
    c = Context({
        'homepage_list': homepage_list,
    })
    return HttpResponse(t.render(c))
    
def search(request):
    sqs = SearchQuerySet().all()
    homepage_list = Page.objects.filter(Dest='home').order_by('-pub_date')[:5]
    
    extra_context = Context({
        'homepage_list': homepage_list,
    })
    
    view = search_view_factory(
        view_class=SearchView,
        template='search/search.html',
        searchqueryset=sqs,
        )
    return view(request)	
    

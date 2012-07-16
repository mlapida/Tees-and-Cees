# Create your views here.
from django.template import Context, loader
from Sites.models import Page
from django.http import HttpResponse

def index(request):
    homepage_list = Page.objects.filter(Dest='home').order_by('-pub_date')[:5]
    t = loader.get_template('apps/home.html')
    c = Context({
        'homepage_list': homepage_list,
    })
    return HttpResponse(t.render(c))
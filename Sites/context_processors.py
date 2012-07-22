from Sites.models import Page, App

def dynamic(request):
    recentadds = App.objects.order_by('-pub_date')[:5]
    sidebarcontent = Page.objects.filter(Dest='sidebar').order_by('-pub_date')[:5]
    c = Context(
    	('recentadds': recentadds),
    	('sidebarcontent': sidebarcontent),
    )
    return {c}
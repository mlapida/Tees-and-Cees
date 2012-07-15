from Sites.models import App
from Sites.models import Points
from django.contrib import admin

class PointsInline(admin.StackedInline):
    model = Points
    extra = 3

class AppAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['Name', 'Address', 'founded', 'founder', 'business_model']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [PointsInline]
    list_display = ('Name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['Name']
    date_hierarchy = 'pub_date'

admin.site.register(App, AppAdmin)


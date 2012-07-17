import datetime
from haystack import indexes
from Sites.models import App
from django.utils import timezone

class AppIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    apps = indexes.CharField(model_attr='Name')
    #pub_date = indexes.DateTimeField(model_attr='pub_date')

    def get_model(self):
        return App

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return self.get_model().objects
        #.filter(pub_date__lte=datetime.datetime.now())
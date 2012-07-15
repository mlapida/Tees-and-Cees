from django.db import models
import datetime
from django.utils import timezone

class App(models.Model):
    Name = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    founded = models.IntegerField()
    founder = models.CharField(max_length=200)
    business_model = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.Name
        
class Points(models.Model):
    App = models.ForeignKey(App)
    point_type = models.CharField(max_length=50)
    importance = models.IntegerField()
    pub_date = models.DateTimeField('date published')
    description = models.CharField(max_length=200)
    def __unicode__(self):
        return self.description


# Create your models here.

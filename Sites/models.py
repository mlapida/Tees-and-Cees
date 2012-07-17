from django.db import models
import datetime
from django.utils import timezone

class App(models.Model):
	Name = models.CharField(max_length=200)
	Address = models.URLField(verify_exists=True, max_length=200)
	founded = models.IntegerField()
	founder = models.CharField(max_length=200)
	business_model = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200)
	pub_date = models.DateTimeField('date published', auto_now_add=True)
	def __unicode__(self):
		return self.Name
        
class Points(models.Model):
	POINT_TYPES = (
		('PP' , 'Privacy Policy'),
		('TC' , 'Terms & Conditions'),
		('G' , 'General'),
	)
	App = models.ForeignKey(App)
	point_type = models.CharField(max_length=50, choices=POINT_TYPES)
	importance = models.IntegerField()
	pub_date = models.DateTimeField('date published', auto_now_add=True)
	description = models.TextField(max_length=500)
	def __unicode__(self):
		return self.description
	def type(self):
		if self.importance <= 50:
			return "info"
		if self.importance <= 75:
			return "warning"
		return "danger"
        
class Page(models.Model):
	Title = models.CharField(max_length=200)
	Body = models.TextField(max_length=1600)
	Author = models.CharField(max_length=200)
	Dest = models.CharField(max_length=20)
	pub_date = models.DateTimeField('date published', auto_now_add=True)
	def __unicode__(self):
		return self.Title        


# Create your models here.

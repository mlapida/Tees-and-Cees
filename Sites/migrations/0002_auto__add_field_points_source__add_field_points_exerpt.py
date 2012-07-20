# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Points.source'
        db.add_column('Sites_points', 'source',
                      self.gf('django.db.models.fields.URLField')(default='n/a', max_length=200),
                      keep_default=False)

        # Adding field 'Points.exerpt'
        db.add_column('Sites_points', 'exerpt',
                      self.gf('django.db.models.fields.TextField')(default='Coming Soon', max_length=500),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Points.source'
        db.delete_column('Sites_points', 'source')

        # Deleting field 'Points.exerpt'
        db.delete_column('Sites_points', 'exerpt')


    models = {
        'Sites.app': {
            'Address': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'Meta': {'object_name': 'App'},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'business_model': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'founded': ('django.db.models.fields.IntegerField', [], {}),
            'founder': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200'})
        },
        'Sites.page': {
            'Author': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'Body': ('django.db.models.fields.TextField', [], {'max_length': '1600'}),
            'Dest': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'Meta': {'object_name': 'Page'},
            'Title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'Sites.points': {
            'App': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Sites.App']"}),
            'Meta': {'object_name': 'Points'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'exerpt': ('django.db.models.fields.TextField', [], {'default': "'Coming Soon'", 'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'importance': ('django.db.models.fields.IntegerField', [], {}),
            'point_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'source': ('django.db.models.fields.URLField', [], {'default': "'n/a'", 'max_length': '200'})
        }
    }

    complete_apps = ['Sites']
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'App'
        db.create_table('Sites_app', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('Address', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('founded', self.gf('django.db.models.fields.IntegerField')()),
            ('founder', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('business_model', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=200)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('Sites', ['App'])

        # Adding model 'Points'
        db.create_table('Sites_points', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('App', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Sites.App'])),
            ('point_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('importance', self.gf('django.db.models.fields.IntegerField')()),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('source', self.gf('django.db.models.fields.URLField')(default='n/a', max_length=200)),
            ('exerpt', self.gf('django.db.models.fields.TextField')(default='Coming Soon', max_length=500)),
        ))
        db.send_create_signal('Sites', ['Points'])

        # Adding model 'Page'
        db.create_table('Sites_page', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('Body', self.gf('django.db.models.fields.TextField')(max_length=1600)),
            ('Author', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('Dest', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('Sites', ['Page'])


    def backwards(self, orm):
        # Deleting model 'App'
        db.delete_table('Sites_app')

        # Deleting model 'Points'
        db.delete_table('Sites_points')

        # Deleting model 'Page'
        db.delete_table('Sites_page')


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
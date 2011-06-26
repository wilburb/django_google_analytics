# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'GoogleAnalytics'
        db.create_table('google_analytics_googleanalytics', (
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'], primary_key=True)),
            ('web_property_id', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
        ))
        db.send_create_signal('google_analytics', ['GoogleAnalytics'])


    def backwards(self, orm):
        
        # Deleting model 'GoogleAnalytics'
        db.delete_table('google_analytics_googleanalytics')


    models = {
        'google_analytics.googleanalytics': {
            'Meta': {'object_name': 'GoogleAnalytics'},
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']", 'primary_key': 'True'}),
            'web_property_id': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['google_analytics']

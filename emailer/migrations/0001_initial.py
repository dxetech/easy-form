# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Key'
        db.create_table('emailer_key', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('server_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('api_key', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
        ))
        db.send_create_signal('emailer', ['Key'])


    def backwards(self, orm):
        # Deleting model 'Key'
        db.delete_table('emailer_key')


    models = {
        'emailer.key': {
            'Meta': {'object_name': 'Key'},
            'api_key': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'server_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['emailer']
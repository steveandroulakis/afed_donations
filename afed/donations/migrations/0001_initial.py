# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Donation'
        db.create_table('donations_donation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('donor_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('donor_address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('donor_suburb', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('donor_postcode', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('donor_state', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('recipient_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('recipient_address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('recipient_suburb', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('recipient_state', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('recipient_postcode', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('transaction_date', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('transaction_value', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('period', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('record_number', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
        ))
        db.send_create_signal('donations', ['Donation'])


    def backwards(self, orm):
        # Deleting model 'Donation'
        db.delete_table('donations_donation')


    models = {
        'donations.donation': {
            'Meta': {'object_name': 'Donation'},
            'donor_address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'donor_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'donor_postcode': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'donor_state': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'donor_suburb': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'period': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'recipient_address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'recipient_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'recipient_postcode': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'recipient_state': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'recipient_suburb': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'record_number': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'transaction_date': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'transaction_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        }
    }

    complete_apps = ['donations']
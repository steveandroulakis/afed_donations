# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Donation.transaction_value'
        db.alter_column('donations_donation', 'transaction_value', self.gf('django.db.models.fields.FloatField')(null=True))

    def backwards(self, orm):

        # Changing field 'Donation.transaction_value'
        db.alter_column('donations_donation', 'transaction_value', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

    models = {
        'donations.donation': {
            'Meta': {'ordering': "['donor_name']", 'object_name': 'Donation'},
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
            'transaction_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'transaction_value': ('django.db.models.fields.FloatField', [], {'null': 'True'})
        }
    }

    complete_apps = ['donations']
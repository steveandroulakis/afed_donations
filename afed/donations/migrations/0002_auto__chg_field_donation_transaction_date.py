# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    no_dry_run = True

    def forwards(self, orm):

        # Changing field 'Donation.transaction_date'
        # import time

        # for donation in orm.Donation.objects.all():
        #     if donation.transaction_date:
        #         try:
        #             d = time.strptime(donation.transaction_date, "%d/%m/%y")
        #             dt = datetime.datetime.fromtimestamp(time.mktime(d))
        #             donation.transaction_date = dt
        #             donation.save()
        #         except ValueError:
        #             donation.transaction_date = None
        #             donation.save()
        db.alter_column('donations_donation', 'transaction_date', self.gf('django.db.models.fields.DateField')(null=True))

    def backwards(self, orm):

        # Changing field 'Donation.transaction_date'
        db.alter_column('donations_donation', 'transaction_date', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

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
            'transaction_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'transaction_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        }
    }

    complete_apps = ['donations']

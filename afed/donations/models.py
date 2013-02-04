from django.db import models


class Donation(models.Model):
    """
    AU federal donations
    """
    donor_name = models.CharField(max_length=255, null=True)
    donor_address = models.CharField(max_length=255, null=True)
    donor_suburb = models.CharField(max_length=255, null=True)
    donor_state = models.CharField(max_length=255, null=True)
    donor_postcode = models.FloatField(null=True)
    donor_state = models.CharField(max_length=255, null=True)
    recipient_name = models.CharField(max_length=255, null=True)
    recipient_address = models.CharField(max_length=255, null=True)
    recipient_suburb = models.CharField(max_length=255, null=True)
    recipient_state = models.CharField(max_length=255, null=True)
    recipient_postcode = models.FloatField(null=True)
    transaction_date = models.DateField(null=True)
    transaction_value = models.FloatField(null=True)
    period = models.CharField(max_length=255, null=True)
    record_number = models.FloatField(null=True)
    source = models.CharField(max_length=255, null=True)

    def __unicode__(self):
        return u"%s" % (self.donor_name)

    class Meta:
        ordering = ['donor_name']

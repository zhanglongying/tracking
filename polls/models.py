from django.db import models

# Create your models here.
class TrackingItem(models.Model):
    tracking_str = models.TextField()
    upload_date = models.DateTimeField('date published')
    is_deal =  models.BooleanField(False)

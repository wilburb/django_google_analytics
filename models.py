from django.db import models
from django.contrib.sites.models import Site

class GoogleAnalytics(models.Model):
    site = models.ForeignKey(Site, primary_key=True)
    web_property_id = models.CharField(blank=True, max_length=15)

    def __unicode__(self):
        return self.site.__unicode__() + " " + self.web_property_id
from django.contrib import admin
from django_site_googleanalytics.models import GoogleAnalytics
from django.contrib.sites import admin

class DjangoSiteGoogleAnalyticsInline(admin.StackedInline):
    model = GoogleAnalytics
    
class SiteAdmin(admin.ModelAdmin):
    inlines = [DjangoSiteGoogleAnalyticsInline]
    
admin.site.unregister(Site)
admin.site.register(Site, SiteAdmin)
from django import template
from google_analytics.models import GoogleAnalytics
from django.contrib.sites.models import Site
register = template.Library()

@register.tag
def google_analytics(parser, token):
    return AnalyticsNode()
    
class AnalyticsNode(template.Node):
    def __init__(self):
        self.site = Site.objects.get_current()
        try:
            self.web_property_id = GoogleAnalytics.objects.filter(site=self.site)[0].web_property_id
        except IndexError:
            self.web_property_id = ''
    def render(self, context):
        if self.web_property_id:
            analytic_template = template.loader.get_template('google_analytics/analytics.html')
            context = template.Context({
                               'web_property_id': self.web_property_id,
                               })
            return analytic_template.render(context)
        else:
            return ''

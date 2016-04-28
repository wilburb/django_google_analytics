from django import template
from analytics.models import GoogleAnalytics
from django.contrib.sites.models import Site
register = template.Library()

@register.tag
def analytics(parser, token):
    return AnalyticsNode()
    
class AnalyticsNode(template.Node):
    def render(self, context):
        current_site = Site.objects.get_current()
        try:
            web_property_id = GoogleAnalytics.objects.get(site=current_site).web_property_id
            analytic_template = template.loader.get_template('google_analytics/analytics.html')
            context = template.Context({
                               'web_property_id': web_property_id,
                               })
            return analytic_template.render(context)
        except GoogleAnalytics.DoesNotExist:
            return ''
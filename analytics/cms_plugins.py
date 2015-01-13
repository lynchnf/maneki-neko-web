from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from analytics.models import GoogleAnalytics

class GoogleAnalyticsPlugin(CMSPluginBase):
    model = GoogleAnalytics
    name = _("Google Analytics")
    render_template = "google_analytics.html"

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context
    
plugin_pool.register_plugin(GoogleAnalyticsPlugin)
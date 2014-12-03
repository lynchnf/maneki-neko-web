from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _
from models import GoogleAnalytics

class GoogleAnalyticsPlugin(CMSPluginBase):
    """
    Plugin for Google Analytics. Writes out necessary JavaScript so that Analytics can be collected on the website.

    The Placeholder should be defined in the main page and should be set with the 'inherit' flag in the base template.
    This will require the plugin to be added only once to the main page. 
    """
    model = GoogleAnalytics
    name = _("Google Analytics")
    module = "Developer"
    render_template = "google_analytics.html"

    def render(self, context, instance, placeholder):
        context['instance'] = instance

        return context

plugin_pool.register_plugin(GoogleAnalyticsPlugin)
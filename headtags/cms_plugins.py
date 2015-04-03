from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from headtags.models import MetaTag

class MetaTagPlugin(CMSPluginBase):
    model = MetaTag
    name = _("Meta Tag")
    render_template = "meta_tag.html"

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context
    
plugin_pool.register_plugin(MetaTagPlugin)
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

class MenuPlugin(CMSPluginBase):
    name = _("Menu")
    render_template = "menu.html"

    def render(self, context, instance, placeholder):
        return context
    
class BreadcrumbPlugin(CMSPluginBase):
    name = _("Breadcrumb")
    cache = False
    render_template = "breadcrumb.html"
    
    def render(self, context, instance, placeholder):
        return context
    
plugin_pool.register_plugin(MenuPlugin)
plugin_pool.register_plugin(BreadcrumbPlugin)
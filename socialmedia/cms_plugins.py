from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from socialmedia.models import SocialLink, ICON_CHOICES

class SocialLinkPlugin(CMSPluginBase):
    model = SocialLink
    name = _("Social Link")
    render_template = "social_link.html"

    def render(self, context, instance, placeholder):
        if instance.size == 1:
            styleClass = "sm fa " + instance.icon + " fa-lg"
        elif instance.size == 2:
            styleClass = "sm fa " + instance.icon + " fa-2x"
        elif instance.size == 3:
            styleClass = "sm fa " + instance.icon + " fa-3x"
        elif instance.size == 4:
            styleClass = "sm fa " + instance.icon + " fa-4x"
        elif instance.size == 5:
            styleClass = "sm fa " + instance.icon + " fa-5x"
        else:
            styleClass = "sm fa " + instance.icon;
        context['styleClass'] = styleClass
        
        title = ""
        for choice in ICON_CHOICES:
            if choice[0] == instance.icon:
                title = choice[1]
        paren_pos = title.find(" (")
        if paren_pos > 0:
            title = title[:paren_pos]
        title.strip()
        context['title'] = title

        context['instance'] = instance
        return context
    
plugin_pool.register_plugin(SocialLinkPlugin)
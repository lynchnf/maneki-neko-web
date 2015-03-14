from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from staff.models import Department
import logging

logger = logging.getLogger(__name__)

class ContactUsPlugin(CMSPluginBase):
    name = _("Contact Us")
    render_template = "contact_us.html"

    def render(self, context, instance, placeholder):
        departments = Department.objects.order_by('-chair','name');
        context['departments'] = departments
        context['instance'] = instance
        return context

plugin_pool.register_plugin(ContactUsPlugin)
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from staff.models import Department
from django.contrib.auth.models import User
from staff.models import Position

import logging

logger = logging.getLogger(__name__)

class ContactUsPlugin(CMSPluginBase):
    name = _("Contact Us")
    render_template = "contact_us.html"

    def render(self, context, instance, placeholder):
        departments = Department.objects.order_by('-chair', 'name')
        context['departments'] = departments
        context['instance'] = instance
        return context
    
class EmailLogPlugin(CMSPluginBase):
    name = _("Email Log")
    render_template = "email_log.html"

    def render(self, context, instance, placeholder):
        
        
        request = context['request']
        current_user = request.user        
        
        context['current_user'] = current_user
        context['instance'] = instance
        return context

class StaffListPlugin(CMSPluginBase):
    name = _("Staff List")
    render_template = "staff_list.html"

    def render(self, context, instance, placeholder):
        user_models = User.objects.filter(is_staff=True).exclude(is_superuser=True).order_by("last_name", "first_name")
        users = []
        for user_model in user_models:
            user = {}
            user["first_name"] = user_model.first_name
            user["last_name"] = user_model.last_name
            user["email"] = user_model.email
            position_models = Position.objects.filter(user__id = user_model.id).order_by("title", "-department__chair", "department__name")
            positions = None
            for position_model in position_models:
                position = None
                if position_model.special_title_name != None:
                    position = position_model.special_title_name
                else:
                    position = position_model.department.name + " " + position_model.get_title_display()
                if positions == None:
                    positions = position
                else:
                    positions = positions + ", " + position
            user["positions"] = positions
            users.append(user)
        context['users'] = users
        context['instance'] = instance
        return context

plugin_pool.register_plugin(ContactUsPlugin)
plugin_pool.register_plugin(EmailLogPlugin)
plugin_pool.register_plugin(StaffListPlugin)
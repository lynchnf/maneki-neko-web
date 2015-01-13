from django.test import TestCase

from cms.api import add_plugin
from cms.models import Placeholder

from analytics.cms_plugins import GoogleAnalyticsPlugin

class SocialLinkPluginTest(TestCase):
    def test_plugin_context(self):
        placeholder = Placeholder.objects.create(slot='test')
        model_instance = add_plugin(
            placeholder,
            GoogleAnalyticsPlugin,
            'en',
            tracking_id = "UA-12345678-1"
        )
        plugin_instance = model_instance.get_plugin_class_instance()
        context = plugin_instance.render({}, model_instance, None)

        model = context['instance']
        self.assertEqual(model.tracking_id, "UA-12345678-1")
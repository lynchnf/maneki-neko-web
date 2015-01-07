from django.test import TestCase

from cms.api import add_plugin
from cms.models import Placeholder

from socialmedia.cms_plugins import SocialLinkPlugin
from socialmedia.models import ICON_CHOICES 

class SocialLinkPluginTest(TestCase):
    def test_plugin_context(self):
        placeholder = Placeholder.objects.create(slot='test')
        model_instance = add_plugin(
            placeholder,
            SocialLinkPlugin,
            'en',
            icon = ICON_CHOICES[17][0],
            size = 1,
            url = "http://mimi-the-maneki-neko.tumblr.com/"
        )
        plugin_instance = model_instance.get_plugin_class_instance()
        context = plugin_instance.render({}, model_instance, None)

        model = context['instance']
        self.assertEqual(model.url, "http://mimi-the-maneki-neko.tumblr.com/")
        self.assertIn('title', context)
        self.assertEqual(context['title'], 'Tumblr')
        self.assertIn('styleClass', context)
        self.assertEqual(context['styleClass'], 'fa fa-tumblr-square fa-lg')
            
    def test_plugin_html(self):
        placeholder = Placeholder.objects.create(slot='test')
        model_instance = add_plugin(
            placeholder,
            SocialLinkPlugin,
            'en',
            icon = ICON_CHOICES[17][0],
            size = 1,
            url = "http://mimi-the-maneki-neko.tumblr.com/"
        )
        html = model_instance.render_plugin({})
        self.assertEqual(html, '<a href="http://mimi-the-maneki-neko.tumblr.com/" title="Tumblr" target="_blank"><i class="fa fa-tumblr-square fa-lg"></i></a>')
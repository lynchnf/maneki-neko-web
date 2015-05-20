import logging

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from news.models import Story


logger = logging.getLogger(__name__)

class NewsDetailsPlugin(CMSPluginBase):
    name = _("News Details")
    render_template = "news_details.html"

    def render(self, context, instance, placeholder):
        story_models = Story.objects.filter(status__in=(2, 3)).order_by('-publish_date', '-id')
        stories = []
        for story_model in story_models:
            story = {}
            story["id"] = story_model.id
            story["title"] = story_model.title
            story["content"] = story_model.content
            story["publish_date"] = story_model.publish_date
            stories.append(story)
        context['stories'] = stories
        context['instance'] = instance
        return context

plugin_pool.register_plugin(NewsDetailsPlugin)

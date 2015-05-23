from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
import logging
from news.models import Story
from news.models import NewsSummary
from news.models import NewsSignUp

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

class NewsSummaryPlugin(CMSPluginBase):
    model = NewsSummary
    name = _("News Summary")
    render_template = "news_summary.html"

    def render(self, context, instance, placeholder):
        story_models = Story.objects.filter(status__in=(2, 3)).order_by('-publish_date', '-id')[:instance.max_stories]
        stories = []
        for story_model in story_models:
            story = {}
            story["id"] = story_model.id
            story["title"] = story_model.title
            story["publish_date"] = story_model.publish_date
            stories.append(story)
        context['stories'] = stories
        context['instance'] = instance
        return context

class NewsSignUpPlugin(CMSPluginBase):
    model = NewsSignUp
    name = _("News Sign Up")
    render_template = "news_sign_up.html"

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(NewsDetailsPlugin)
plugin_pool.register_plugin(NewsSummaryPlugin)
plugin_pool.register_plugin(NewsSignUpPlugin)
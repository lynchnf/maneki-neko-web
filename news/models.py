from cms.models.fields import PageField
from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _


STATUS_CHOICES = (
    (1, _("Draft")),
    (2, _("Publish")),
    (3, _("Email")),
    (4, _("Archive")))

class Story(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    status = models.IntegerField(default=1, choices=STATUS_CHOICES)
    publish_date = models.DateField(blank=True, null=True)
    email_timestamp = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        verbose_name = "news story"
        verbose_name_plural = "news stories"

    def __unicode__(self):
        return self.title

class NewsSummary(CMSPlugin):
    max_stories = models.IntegerField("Maximum Stories to Show", default=5)
    news_details_page = PageField()

class NewsSignUp(CMSPlugin):
    url = models.URLField("Sign Up Form URL")

    def __unicode__(self):
        return self.url

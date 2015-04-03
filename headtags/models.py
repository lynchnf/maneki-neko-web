from cms.models.pluginmodel import CMSPlugin

from django.db import models

class MetaTag(CMSPlugin):
    http_equiv = models.CharField(max_length=225, blank=True, null=True)
    name = models.CharField(max_length=225, blank=True, null=True)
    content = models.CharField(max_length=225, blank=True, null=True)
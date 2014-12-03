from cms.models import CMSPlugin
from django.db import models

class GoogleAnalytics(CMSPlugin):
    """
    Data for a Google Analytics plugin.
    """
    property_id = models.CharField(max_length=20)
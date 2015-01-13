from cms.models.pluginmodel import CMSPlugin
from django.db import models

class GoogleAnalytics(CMSPlugin):
    
    tracking_id = models.CharField("Google Analytics Tracking ID", max_length=20)    

    def __unicode__x(self):
        return self.tracking_id
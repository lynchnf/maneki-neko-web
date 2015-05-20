from datetime import date

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
    publish_date = models.DateField(default=date.today, blank=True, null=True)
    
    class Meta:
        verbose_name = "news story"
        verbose_name_plural = "news stories"

    def __unicode__(self):
        return self.title

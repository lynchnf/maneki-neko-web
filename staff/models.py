from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

TITLE_CHOICES = (
    (1, _("Head")),
    (2, _("Second")),
    (3, _("Staff")))

class Department(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    chair = models.BooleanField()
    
    def __unicode__(self):
        return self.name    
    
class Position(models.Model):
    user = models.ForeignKey(User)     
    department = models.ForeignKey(Department)     
    title = models.IntegerField(choices=TITLE_CHOICES)

    def __unicode__(self):
        return "%s - %s (%s)" % (self.department.name, self.user.get_full_name(), self.get_title_display())    

class ContactUsLog(models.Model):
    from_email = models.EmailField()
    to_department = models.CharField(max_length=100)
    to_email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField()
    sent_successfully = models.BooleanField()
    
    def __unicode__(self):
        return "%s: %s" % (self.to_department, self.subject)
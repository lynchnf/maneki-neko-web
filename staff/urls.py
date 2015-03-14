from django.conf.urls import patterns, url
from staff.views import contact_us

urlpatterns = patterns('',
    url(r'^contact_us/$', contact_us, name='contact_us')
)
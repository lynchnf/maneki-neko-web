from django.conf.urls import patterns, url

from staff.views import contact_us
from staff.views import email_instance
from staff.views import email_list
from staff.views import email_reply


urlpatterns = patterns('',
    url(r'^contact_us/$', contact_us, name='contact_us'),
    url(r'^email_instance/$', email_instance, name='email_instance'),
    url(r'^email_list/$', email_list, name='email_list'),
    url(r'^email_reply/$', email_reply, name='email_reply')
)

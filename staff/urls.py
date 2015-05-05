from django.conf.urls import patterns, url
from staff.views import contact_us, email_instance, email_list

urlpatterns = patterns('',
    url(r'^contact_us/$', contact_us, name='contact_us'),
    url(r'^email_instance/$', email_instance, name='email_instance'),
    url(r'^email_list/$', email_list, name='email_list')
)
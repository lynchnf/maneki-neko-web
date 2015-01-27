from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

from django.db import models

ICON_CHOICES = (
        ("fa-delicious", _("Delicious")),
        ("fa-digg", _("Digg")),
        ("fa-facebook", _("Facebook")),
        ("fa-flickr", _("Flickr")),
        ("fa-google-plus", _("Google+")),
        ("fa-instagram", _("Instagram")),
        ("fa-linkedin", _("LinkedIn")),
        ("fa-map-marker", _("Map")),
        ("fa-pinterest", _("Pinterest")),
        ("fa-rss", _("RSS feed")),
        ("fa-reddit", _("reddit")),
        ("fa-spotify", _("Spotify")),
        ("fa-stumbleupon", _("StumbleUpon")),
        ("fa-tumblr", _("Tumblr")),
        ("fa-twitter", _("Twitter")),
        ("fa-youtube-play", _("YouTube")))

class SocialLink(CMSPlugin):
    icon = models.CharField("Social Network Icon", max_length=20, choices=ICON_CHOICES)
    size = models.IntegerField("Icon Size", default=0)
    url = models.URLField("URL")

    def __unicode__(self):
        return "icon is %s, size is %s, url is %s" % (self.icon, self.size, self.url)
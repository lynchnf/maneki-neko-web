from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

from django.db import models

ICON_CHOICES = (
        ("fa-delicious", _("Delicious")),
        ("fa-digg", _("Digg")),
        ("fa-facebook", _("Facebook")),
        ("fa-facebook-square", _("Facebook (square)")),
        ("fa-flickr", _("Flickr")),
        ("fa-foursquare", _("Foursquare")),
        ("fa-google-plus", _("Google+")),
        ("fa-google-plus-square", _("Google+ (square)")),
        ("fa-instagram", _("Instagram")),
        ("fa-pinterest", _("Pinterest")),
        ("fa-pinterest-square", _("Pinterest (square)")),
        ("fa-reddit", _("Reddit")),
        ("fa-reddit-square", _("Reddit (square)")),
        ("fa-spotify", _("Spotify")),
        ("fa-stumbleupon", _("StumbleUpon")),
        ("fa-stumbleupon-circle", _("StumbleUpon (circle)")),
        ("fa-tumblr", _("Tumblr")),
        ("fa-tumblr-square", _("Tumblr (square)")),
        ("fa-twitter", _("Twitter")),
        ("fa-twitter-square", _("Twitter (square)")))

class SocialLink(CMSPlugin):
    icon = models.CharField("Social Network Icon", max_length=20, choices=ICON_CHOICES)
    size = models.IntegerField("Icon Size", default=0)
    url = models.URLField("URL")
    
    def __unicode__(self):
        return self.url
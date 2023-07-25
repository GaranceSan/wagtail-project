from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting,register_setting

@register_setting
class Socialmediasettings(BaseSiteSetting):

    facebook = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)

    panels=[
        MultiFieldPanel([
            FieldPanel("facebook"),
            FieldPanel("youtube")

        ], heading="Social media settings")
]

# Create your models here.

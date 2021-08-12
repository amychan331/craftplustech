from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.images.edit_handlers import ImageChooserPanel


@register_setting
class MetadataSettings(BaseSetting):
  author = models.TextField(blank=True, null=True, help_text="Site Author")
  description = models.TextField(blank=True, null=True, help_text="Site Description")

  panels = [
    MultiFieldPanel({
      FieldPanel("author"),
      FieldPanel("description"),
    }, heading="Metadata Settings")
  ]


@register_setting
class FooterSettings(BaseSetting):
  footer_text = models.TextField(blank=True, null=True, help_text="Copyright text after the year")
  footer_image = models.ForeignKey(
    "wagtailimages.Image",
    blank=True,
    null=True,
    related_name="+",
    on_delete=models.SET_NULL,
  )

  panels = [
    MultiFieldPanel({
      FieldPanel("footer_text"),
      ImageChooserPanel("footer_image"),
    }, heading="Footer Settings")
  ]


@register_setting
class SocialMediaSettings(BaseSetting):
  twitter = models.URLField(blank=True, null=True, help_text="Twitter URL")
  linkedin = models.URLField(blank=True, null=True, help_text="Linkedin URL")
  github = models.URLField(blank=True, null=True, help_text="Github URL")
  devto = models.URLField(blank=True, null=True, help_text="DEV URL")

  panels = [
    MultiFieldPanel({
      FieldPanel("twitter"),
      FieldPanel("linkedin"),
      FieldPanel("github"),
      FieldPanel("devto"),
    }, heading="Social Media Settings")
  ]
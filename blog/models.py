import datetime

from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtailcodeblock.blocks import CodeBlock
from streams import blocks

# Create your models here.
class BlogListingPage(Page):
  """Listing page lists all the Blog Detail Pages"""

  custom_title = models.CharField(
    max_length=100,
    blank=False,
    null=False,
    help_text='Overwrites default title',
  )

  content_panels = Page.content_panels + [
    FieldPanel("custom_title"),
  ]

  def get_context(self, request, *args, **kwargs):
    """Adding custom stuff to our context"""
    context = super().get_context(request, *args, **kwargs)
    context["posts"] = BlogDetailPage.objects.live().public().order_by('-published_date')
    return context


class BlogDetailPage(Page):
  """Blog detail page"""

  custom_title = models.CharField(
    max_length=100,
    blank=False,
    null=False,
    help_text='Overwrites default title',
  )
  published_date = models.DateField(
    "Published Date",
    default=datetime.date.today
  )
  blog_image = models.ForeignKey(
    "wagtailimages.Image",
    blank=True,
    null=True,
    related_name="+",
    on_delete=models.SET_NULL,
  )

  content = StreamField(
    [
      ("title_and_text", blocks.TitleAndTextBlock()),
      ("simple_richtext", blocks.SimpleRichtextBlock()),
      ("full_richtext", blocks.RichtextBlock()),
      ("codeblock", CodeBlock(label='Code')),
    ],
    null=True,
    blank=True,
  )

  content_panels = Page.content_panels + [
    FieldPanel("custom_title"),
    FieldPanel('published_date'),
    ImageChooserPanel("blog_image"),
    StreamFieldPanel("content"),
  ]

  class Meta:
    verbose_name="Blog Post"
    verbose_name_plural = "Blog Posts"
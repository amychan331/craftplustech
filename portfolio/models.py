from django.db import models

from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from streams import blocks


class Portfolio(Page):
    """Portfolio page model."""

    template = "portfolio/portfolio_page.html"

    intro_text = StreamField(
      [
        ("title_and_text", blocks.TitleAndTextBlock()),
        ("simple_richtext", blocks.SimpleRichtextBlock()),
        ("full_richtext", blocks.RichtextBlock()),
      ],
      null=True,
      blank=True,
    )

    content = StreamField(
      [ ("projectblock", blocks.ProjectBlock()) ],
      null=True,
      blank=True,
    )

    content_panels = Page.content_panels + [
      StreamFieldPanel("intro_text"),
      StreamFieldPanel("content"),
    ]

    class Meta:

        verbose_name = "Portfolio Page"
        verbose_name_plural = "Portfolio Pages"
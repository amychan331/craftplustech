"""Stream fields"""

from wagtail.core import blocks
from wagtail.core.templatetags.wagtailcore_tags import richtext
from wagtail.images.blocks import ImageChooserBlock


class TitleAndTextBlock(blocks.StructBlock):
  """Title and text and nothing else."""

  title = blocks.CharBlock(required=True, help_text='Add title')
  text = blocks.TextBlock(required=True, help_text='Add additional text')

  class Meta: #noqa
    template = "streams/title_and_text_block.html"
    icon = "edit"
    label = "Title & Text"


class RichtextBlock(blocks.RichTextBlock):
    """Richtext with all the features."""

    def get_api_representation(self, value, context=None):
        return richtext(value.source)

    class Meta:  # noqa
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = "Full RichText"


class SimpleRichtextBlock(blocks.RichTextBlock):
  """Richtext without (limited) all the features."""

  def __init__(
    self, required=True, help_text=None, editor="default", features=None, **kwargs
  ): #noqa
    super().__init__(**kwargs)
    self.features = ["bold", "italic", "link"]

  class Meta: #noqa
    template = "streams/richtext_block.html"
    icon = "edit"
    label = "Simple RichText"


class ProjectBlock(blocks.StructBlock):
  """Project list item"""

  title = blocks.CharBlock(required=True, help_text="Project title")
  uid = blocks.CharBlock(required=True, help_text="Unique Project ID")
  content = blocks.TextBlock(required=True, help_text="Project detail")
  url = blocks.URLBlock(required=False, help_text='Project link')
  slides = blocks.ListBlock(
    blocks.StructBlock(
      [
        ("image", ImageChooserBlock(required=True)),
        ("alt", blocks.CharBlock(required=True, max_length=100))
      ]
    )
  )

  class Meta: #noqa
    template = "streams/project_block.html"
    icon = "image"
    label = "Project"

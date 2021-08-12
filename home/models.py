import json
import time

from django.conf import settings
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
import django.forms

from modelcluster.fields import ParentalKey
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import (
  FieldPanel,
  FieldRowPanel,
  InlinePanel,
  MultiFieldPanel
)
from wagtail.contrib.forms.forms import FormBuilder
from wagtail.contrib.forms.models import (
  AbstractEmailForm,
  AbstractFormField,
  AbstractFormSubmission
)

from bs4 import BeautifulSoup


class FormField(AbstractFormField):
  page = ParentalKey(
        'HomePage',
        on_delete=models.CASCADE,
        related_name='form_fields',
  )


class CustomFormBuilder(FormBuilder):

    def create_multiline_field(self, field, options):
        options['max_length'] = 600
        return django.forms.CharField(widget=django.forms.Textarea, **options)


class HomePage(AbstractEmailForm):
    template = 'home/home_page.html'
    landing_page_template = "home/home_page_landing.html"

    max_count = 1

    body = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    form_builder = CustomFormBuilder

    content_panels = AbstractEmailForm.content_panels + [
      FieldPanel('body', classname="full"),
      InlinePanel('form_fields', label='Form Fields'),
      FieldPanel('thank_you_text'),
      MultiFieldPanel([
        FieldRowPanel([
          FieldPanel('from_address', classname="col6"),
          FieldPanel('to_address', classname="col6"),
        ]),
        FieldPanel("subject"),
      ], heading="Homepage Settings")
    ]

    def serve(self, request, *args, **kwargs):
      if request.method == 'POST':
        form = self.get_form(request.POST, request.FILES, page=self, user=request.user)

        # Check for timestamp, honeypot, and form validation
        current = int(time.time())
        ts_differences = current - int(request.POST['ts'])
        has_html = bool(BeautifulSoup(request.POST['what_is_you_message'], "html.parser").find())
        if (has_html):
          form = self.get_form(page=self, user=request.user)
          form.bot_error = "Please use text only."
        elif (current > 0 and
           ts_differences > 3 and
           request.POST['name_not'] == '' and
           form.is_valid()):
            form_submission = self.process_form_submission(form)
            return self.render_landing_page(request, form_submission, *args, **kwargs)
        else:
          form = self.get_form(page=self, user=request.user)
          form.bot_error = "We're sorry, the form could not be sent at the moment. Please try again later or contact me via one of the social media options."
      else:
        form = self.get_form(page=self, user=request.user)

      context = self.get_context(request)
      context['form'] = form
      return TemplateResponse(
        request,
        self.get_template(request),
        context
      )


class CustomFormSubmission(AbstractFormSubmission):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

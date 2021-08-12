"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv

from django.core.wsgi import get_wsgi_application

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

if os.getenv('DJANGO_SETTINGS_MODULE'):
  os.environ['DJANGO_SETTINGS_MODULE'] = os.getenv('DJANGO_SETTINGS_MODULE')
else:
  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings.dev")

application = get_wsgi_application()

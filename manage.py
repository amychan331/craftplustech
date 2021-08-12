#!/usr/bin/env python
import os
import sys
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

if __name__ == "__main__":

    if os.getenv('DJANGO_SETTINGS_MODULE'):
        os.environ['DJANGO_SETTINGS_MODULE'] = os.getenv('DJANGO_SETTINGS_MODULE')
    else:
      os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings.dev")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
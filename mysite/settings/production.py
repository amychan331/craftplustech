from .base import *
import os

DEBUG = False

ALLOWED_HOSTS = ['craftplustech.com']

SECRET_KEY = os.environ.get('SECRET_KEY')

try:
    from .local import *
except ImportError:
    pass

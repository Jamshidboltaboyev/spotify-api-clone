from os import environ

from .base import *

STATIC_ROOT = '/app/data/static_root'

SECRET_KEY = environ.get('PRODUCTION_SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['django', '0.0.0.0']

from .base import *


MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

INSTALLED_APPS += ['debug_toolbar']

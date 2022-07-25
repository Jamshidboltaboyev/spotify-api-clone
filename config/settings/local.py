from .base import *

######################################
# django-debug-toolbar  start
######################################


INSTALLED_APPS += [
    'debug_toolbar',
    "django_extensions"
]

MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')

# docker network list | grep ${PWD##*/} | sed -r 's/^([0-9a-z]+).*$/\1/' | xargs docker network inspect  \
# --format "{{ range .IPAM.Config }}{{ .Gateway }}
INTERNAL_IPS = [
    "172.18.0.1"
]

DEBUG_TOOLBAR_PANELS = [
    # 'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

######################################
# django-debug-toolbar  end
######################################

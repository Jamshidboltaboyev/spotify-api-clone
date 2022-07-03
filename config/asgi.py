# Stdlib imports
import os

# Core django imports
from django.core.asgi import get_asgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_asgi_application()

"""
ASGI config for taps_rezos project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# settings_module ='taps_backend.deployment' if 'RENDER_EXTERNAL_HOSTNAME' in os.environ else 'taps_rezos.settings'
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taps_rezos.settings')

application = get_asgi_application()

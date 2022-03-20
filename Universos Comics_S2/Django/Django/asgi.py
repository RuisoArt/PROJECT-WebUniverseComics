"""
ASGI config for Django project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
#from django.core.asgi import get_asgi_application
from channels.http import AsgiHandler
import my_app.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Django.settings")

application = ProtocolTypeRouter({
    "http": AsgiHandler(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            my_app.routing.websocket_urlpatterns
        )
    ),
})


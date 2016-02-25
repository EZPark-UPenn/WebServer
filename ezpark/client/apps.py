from __future__ import unicode_literals

from django.apps import AppConfig


class ClientConfig(AppConfig):
    name = 'client'

    def ready(self):
        from client import signals

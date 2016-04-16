from __future__ import unicode_literals

from django.apps import AppConfig
from hw.hwInterface import showReady

class GameConfig(AppConfig):
    name = 'game'
    def ready(self):
        showReady()
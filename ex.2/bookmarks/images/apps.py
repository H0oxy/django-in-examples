from django.apps import AppConfig
from django.db.models import Count


class ImagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'images'


def ready(self):
    import images.signals
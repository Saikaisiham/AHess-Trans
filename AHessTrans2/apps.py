from django.apps import AppConfig


class Ahesstrans2Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AHessTrans2'


    def ready(self):
        import AHessTrans2.signals
from django.apps import AppConfig


class LoginConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # name must contain the whole path in order to be recognized
    name = 'shapeyourbot.apps.authentication'

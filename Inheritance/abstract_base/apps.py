from django.apps import AppConfig


class AbstractBaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'abstract_base'

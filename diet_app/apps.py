"""Diet apps."""
# Django
from django.apps import AppConfig


class DietAppConfig(AppConfig):  # noqa: D101
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'diet_app'

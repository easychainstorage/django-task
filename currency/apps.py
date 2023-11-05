"""AppConfig for the 'currency' app."""
from django.apps import AppConfig


class CurrencyConfig(AppConfig):
    """Currency config."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "currency"

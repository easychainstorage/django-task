"""Admin."""
from django.contrib import admin
from .models import ExchangeRate, Currency


class ExchangeRateAdmin(admin.ModelAdmin):
    """
    Admin class for display ExchangeRate
    object and filter in the Django admin interface.
    """

    list_filter = [
        "currency_pair",
        "date",
    ]
    list_display = ("currency_pair", "rate", "date")


class CurrencyAdmin(admin.ModelAdmin):
    """
    Admin class for display Currency objects
    in the Django admin interface.
    """

    list_display = (
        "symbol",
        "base_currency",
        "target_currency",
    )


admin.site.register(ExchangeRate, ExchangeRateAdmin)
admin.site.register(Currency, CurrencyAdmin)

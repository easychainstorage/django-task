"""Models."""
from django.db import models


class Currency(models.Model):
    """Model for currency base on symol, base_currency and target_currency."""

    symbol = models.CharField(max_length=7, primary_key=True)
    base_currency = models.CharField(max_length=3, default=None)
    target_currency = models.CharField(max_length=3, default=None)

    def __str__(self):
        return self.symbol


class ExchangeRate(models.Model):
    """Model for exchange rate for a currency pair at a specific date."""

    currency_pair = models.ForeignKey(Currency,
                                      on_delete=models.CASCADE,
                                      related_name='base_rates',
                                      default=None)
    rate = models.DecimalField(max_digits=20, decimal_places=6)
    date = models.DateField()

    def __str__(self):
        return str(self.currency_pair)

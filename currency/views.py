"""API view."""
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from .models import Currency
from .serializers import CurrencySerializer


class ListCurrency(generics.ListAPIView):
    """View for currency pair list available in local database."""

    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["base_currency", "target_currency"]

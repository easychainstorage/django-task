from rest_framework import serializers
from .models import Currency


class CurrencySerializer(serializers.ModelSerializer):
    """Serializer for Currency model."""
    class Meta:
        model = Currency
        fields = ("symbol",)

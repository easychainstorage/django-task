"""Tests."""
from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from .models import Currency, ExchangeRate


class CurrencyTests(TestCase):
    """ Test cases for the Currency and ExchangeRate models."""
    @classmethod
    def setUpTestData(cls):
        """Set up test data for the test cases."""
        cls.currency1 = Currency.objects.create(
            symbol="USD/EUR",
            base_currency="USD",
            target_currency="EUR",
        )
        cls.currency2 = Currency.objects.create(
            symbol="EUR/GBP",
            base_currency="EUR",
            target_currency="GBP",
        )
        cls.currency3 = Currency.objects.create(
            symbol="USD/JPY",
            base_currency="USD",
            target_currency="JPY",
        )
        cls.exchange_rate = ExchangeRate.objects.create(
            currency_pair=cls.currency1,
            rate=1.0018634796,
            date="2022-11-08",
        )

    def test_currency_model_content(self):
        """Test the content of the Currency model."""
        self.assertEqual(self.currency1.symbol, "USD/EUR")
        self.assertEqual(self.currency1.base_currency, "USD")
        self.assertEqual(self.currency1.target_currency, "EUR")

    def test_currency_list_api_view(self):
        """Test the Currency list API view."""
        response = self.client.get(reverse("currency_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Currency.objects.count(), 3)
        self.assertContains(response, self.currency1.symbol)

    def test_exchange_rate_model_content(self):
        """Test the content of the ExchangeRate model."""
        self.assertEqual(self.exchange_rate.currency_pair.symbol, "USD/EUR")
        self.assertEqual(self.exchange_rate.rate, 1.0018634796)
        self.assertEqual(self.exchange_rate.date, "2022-11-08")

    def test_filter_currencies(self):
        """Test filtering currencies through the API."""
        url = reverse("currency_list")
        response_base_currency = self.client.get(
            url + "?base_currency=USD&target_currency="
        )
        self.assertContains(response_base_currency, self.currency1)
        response_target_currency = self.client.get(
            url + "?base_currency=&target_currency=GBP"
        )
        self.assertContains(response_target_currency, self.currency2)
        response_both_currency = self.client.get(
            url + "?base_currency=USD&target_currency="
        )
        self.assertContains(response_both_currency, self.currency3)

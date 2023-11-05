"""Urls for currency app."""
from django.urls import path

from .views import ListCurrency

urlpatterns = [path("", ListCurrency.as_view(), name="currency_list")]

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    CurrencyAPIView, CurrencyAPIListView, ExchangeRateAPIView, ExchangeRateAPIListView
)

urlpatterns = [
    url(r'^currency/$', CurrencyAPIListView.as_view(), name='api-currency'),
    url(r'^currency/(?P<pk>[0-9]+)/$', CurrencyAPIView.as_view(), name='api-currency-detail'),
    url(r'^exchange-rate/$', ExchangeRateAPIListView.as_view(), name='api-exchangerate'),
    url(r'^exchange-rate/(?P<pk>[0-9]+)/$', ExchangeRateAPIView.as_view(), name='api-exchangerate-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

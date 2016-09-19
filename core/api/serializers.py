from rest_framework.serializers import ModelSerializer

from core.models import (
    Currency, ExchangeRate
)


class CurrencySerializer(ModelSerializer):
    class Meta:
        model = Currency
        fields = ["id", "sk", "code", "name", "is_fund", "is_complimentary", "is_metal"]


class ExchangeRateSerializer(ModelSerializer):
    currency = CurrencySerializer()

    class Meta:
        model = ExchangeRate
        fields = ["currency", "exchange_rate", "start_date", "end_date"]

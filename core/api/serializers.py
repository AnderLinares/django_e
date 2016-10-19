from rest_framework.serializers import ModelSerializer

from core.models import (
    Currency, ExchangeRate, ProductBrand, ProductModel,
    VehicleBrand, VehicleModel)


class CurrencySerializer(ModelSerializer):
    class Meta:
        model = Currency
        fields = "__all__"


class ExchangeRateSerializer(ModelSerializer):
    currency = CurrencySerializer()

    class Meta:
        model = ExchangeRate
        fields = "__all__"


class ProductBrandSerializer(ModelSerializer):
    class Meta:
        model = ProductBrand
        fields = "__all__"


class ProductModelSerializer(ModelSerializer):
    brand = ProductBrandSerializer()

    class Meta:
        model = ProductModel
        fields = "__all__"


class VehicleBrandSerializer(ModelSerializer):
    class Meta:
        model = VehicleBrand
        fields = "__all__"


class VehicleModelSerializer(ModelSerializer):
    brand = ProductBrandSerializer()

    class Meta:
        model = VehicleModel
        fields = "__all__"

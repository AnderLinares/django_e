from rest_framework.serializers import ModelSerializer

from core.models import (
    Currency, ExchangeRate, ProductBrand, ProductModel,
    VehicleBrand, VehicleModel, VehicleEnrollment,
    Labour, LabourCategory,
    HandWork, HandWorkCategory)


class HandWorkCategorySerializer(ModelSerializer):
    class Meta:
        model = HandWorkCategory
        fields = "__all__"


class HandWorkSerializer(ModelSerializer):
    # handwork_category = HandWorkCategorySerializer()

    class Meta:
        model = HandWork
        fields = "__all__"





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


class VehicleEnrollmentSerializer(ModelSerializer):
    class Meta:
        model = VehicleEnrollment
        fields = "__all__"


class LabourCategorySerializer(ModelSerializer):
    class Meta:
        model = LabourCategory
        fields = "__all__"


class LabourSerializer(ModelSerializer):
    class Meta:
        model = Labour
        fields = "__all__"

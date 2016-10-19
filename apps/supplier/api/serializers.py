from rest_framework.serializers import ModelSerializer

from apps.product.api.serializers import ProductSerializer
from apps.supplier.models import (
    Supplier, SupplierSubsidiary, SupplierProduct
)


class SupplierSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"


class SupplierSubsidiarySerializer(ModelSerializer):
    supplier = SupplierSerializer()

    class Meta:
        model = SupplierSubsidiary
        fields = "__all__"


class SupplierProductSerializer(ModelSerializer):
    supplier = SupplierSerializer()
    product = ProductSerializer(many=True)

    class Meta:
        model = SupplierProduct
        fields = "__all__"

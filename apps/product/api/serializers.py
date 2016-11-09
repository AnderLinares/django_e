from rest_framework.serializers import ModelSerializer

from apps.product.models import (
   ProductCategory, Product
)


class ProductCategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    product_category = ProductCategorySerializer()

    class Meta:
        model = Product
        fields = "__all__"

from rest_framework.serializers import ModelSerializer

from apps.product.models import (
   ProductCategory, ProductSubCategory, Product
)


class ProductCategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"


class ProductSubCategorySerializer(ModelSerializer):
    product_category = ProductCategorySerializer()

    class Meta:
        model = ProductSubCategory
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    product_category = ProductCategorySerializer()
    product_subcategory = ProductSubCategorySerializer()

    class Meta:
        model = Product
        fields = "__all__"

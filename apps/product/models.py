from django.db import models

from core import constants as core_constants
from core.models import ProductBrand, ProductModel, UnitMeasurement
from core.utils.fields import BaseModel


class ProductCategory(BaseModel):
    name = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        unique_together = ["name"]

    def __str__(self):
        return self.name


class ProductSubCategory(BaseModel):
    product_category = models.ForeignKey(
        ProductCategory, related_name="%(app_label)s_%(class)s_product_category")
    name = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        unique_together = ["product_category", "name"]

    def __str__(self):
        return self.name


class Product(BaseModel):
    product_category = models.ForeignKey(
        ProductCategory, related_name="%(app_label)s_%(class)s_product_category")
    product_subcategory = models.ForeignKey(
        ProductSubCategory, related_name="%(app_label)s_%(class)s_product_subcategory")
    name = models.CharField(max_length=200, null=False, blank=False)
    brand = models.ForeignKey(ProductBrand, related_name="%(app_label)s_%(class)s_brand")
    model = models.ForeignKey(ProductModel, related_name="%(app_label)s_%(class)s_model")
    unit = models.ForeignKey(
        UnitMeasurement, related_name="%(app_label)s_%(class)s_unit",
        limit_choices_to={'type_measurement__in': [
            core_constants.CODE_MEASUREMENT_PURCHASE_LIQUID_UNIT,
            core_constants.CODE_MEASUREMENT_PURCHASE_SOLID_UNIT]})
    sale_price = models.DecimalField(max_digits=8, decimal_places=2, default=0, null=True, blank=True)
    purchase_price = models.DecimalField(max_digits=8, decimal_places=2, default=0, null=True, blank=True)
    picture = models.ImageField(upload_to='product/', blank=True, null=True)

    class Meta:
        unique_together = ["product_category", "product_subcategory", "name"]

    def __str__(self):
        return self.name


class ProductDetail(BaseModel):
    product = models.OneToOneField(
        Product, related_name="%(app_label)s_%(class)s_product")
    series = models.CharField(max_length=200, null=True, blank=True)
    origin = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=200, null=True, blank=True)

    class Meta:
        unique_together = ["product", "series"]

    def __str__(self):
        return self.product.name
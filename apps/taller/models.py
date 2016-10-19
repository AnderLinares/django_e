from django.db import models

from apps.customer.models import UserProfile
from apps.product.models import (
    ProductCategory, ProductSubCategory, Product)
from apps.vehicle.models import Vehicle
from apps.company.models import Subsidiary
from core.utils.fields import BaseModel


class Labour(BaseModel):
    name = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        unique_together = ["name"]

    def __str__(self):
        return self.name


class PurchaseOrderStore(BaseModel):
    """ orden de pedido almacén """
    subsidiary = models.ManyToManyField(
        Subsidiary, related_name="%(app_label)s_%(class)s_subsidiary")
    applicant = models.ForeignKey(UserProfile, related_name="%(app_label)s_%(class)s_applicant")
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}".format(str(self.subsidiary), str(self.applicant))


class PurchaseOrderStoreDetail(BaseModel):
    purchase_order_store = models.ForeignKey(
        PurchaseOrderStore, related_name="%(app_label)s_%(class)s_purchase_order_store")
    vehicle = models.ForeignKey(Vehicle, related_name="%(app_label)s_%(class)s_vehicle")
    product_category = models.ForeignKey(
        ProductCategory, related_name="%(app_label)s_%(class)s_product_category")
    product_subcategory = models.ForeignKey(
        ProductSubCategory, related_name="%(app_label)s_%(class)s_product_subcategory")
    product = models.ForeignKey(
        Product, related_name="%(app_label)s_%(class)s_product")
    description = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    observation = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{0}-{1}".format(str(self.vehicle), str(self.purchase_order_store.subsidiary))

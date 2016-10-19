from django.db import models

from apps.company.models import Subsidiary
from apps.product.models import Product
from core import constants as core_constants
from core.utils.fields import BaseModel


class Supplier(BaseModel):
    business_name = models.CharField(max_length=200, blank=True, null=True, unique=True)
    document_type = models.CharField(
        max_length=20, null=False, blank=False,
        choices=[core_constants.SIS_DOCUMENT_RUC_STRING])
    document_number = models.CharField(max_length=20, null=False, blank=False)
    home_phone = models.CharField(max_length=50, blank=True, null=True)
    mobile_phone = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    contact = models.CharField(max_length=200, blank=True, null=True)
    phone_contact = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        unique_together = ["business_name"]

    def __str__(self):
        return self.business_name


class SupplierSubsidiary(BaseModel):
    supplier = models.OneToOneField(
        Supplier, related_name="%(app_label)s_%(class)s_supplier")
    subsidiary = models.ManyToManyField(
        Subsidiary, related_name="%(app_label)s_%(class)s_subsidiary")

    def get_subsidiary_list(self):
        return "\n".join([p.subsidiary_name for p in self.subsidiary.all()])

    class Meta:
        unique_together = ["supplier"]

    def __str__(self):
        return self.supplier.business_name


class SupplierProduct(BaseModel):
    supplier = models.OneToOneField(
        Supplier, related_name="%(app_label)s_%(class)s_supplier")
    product = models.ManyToManyField(
        Product, related_name="%(app_label)s_%(class)s_product")

    def get_product_list(self):
        return "\n".join([product.name for product in self.product.all()])

    class Meta:
        unique_together = ["supplier"]

    def __str__(self):
        return "{0}-{1}".format(str(self.supplier), str(self.product.name))

from django.db import models

# Create your models here.
from core.utils.fields import BaseModel
from apps.supplier.models import Supplier, SupplierProduct
from apps.company.models import Organization
from core.models import Currency, ExchangeRate, Store
from apps.product.models import ProductCategory, ProductSubCategory, Product


class PurchaseOrder(BaseModel):
    date = models.DateField()
    organization = models.ForeignKey(Organization, related_name="%(app_label)s_%(class)s_organization")
    supplier = models.ForeignKey(Supplier, related_name="%(app_label)s_%(class)s_supplier")
    supplier_product = models.ForeignKey(SupplierProduct, related_name="%(app_label)s_%(class)s_supplier_product")
    currency = models.ForeignKey(Currency, related_name="%(app_label)s_%(class)s_currency")
    exchange_rate = models.ForeignKey(ExchangeRate, related_name="%(app_label)s_%(class)s_exchange_rate")
    store = models.ForeignKey(Store, related_name="%(app_label)s_%(class)s_store")
    igv_tax = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    sub_total = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    total_paid = models.DecimalField(max_digits=18, decimal_places=2, default=0)

    def __str__(self):
        return "{0}".format(str(self.date))


class PurchaseOrderDetail(BaseModel):
    purchase_order = models.ForeignKey(
        PurchaseOrder, related_name="%(app_label)s_%(class)s_purchase_order")
    product_category = models.ForeignKey(
        ProductCategory, related_name="%(app_label)s_%(class)s_product_category")
    product_subcategory = models.ForeignKey(
        ProductSubCategory, related_name="%(app_label)s_%(class)s_product_subcategory")
    product = models.ForeignKey(
        Product, related_name="%(app_label)s_%(class)s_product")
    description = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    unit_price = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    amount_price = models.DecimalField(max_digits=18, decimal_places=2, default=0)

    def __str__(self):
        return "{0}".format(str(self.purchase_order))




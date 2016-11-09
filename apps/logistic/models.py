from django.db import models

from apps.company.models import Organization
from apps.customer.models import User
from apps.product.models import ProductCategory, Product
from apps.supplier.models import Supplier, SupplierProduct
from core.models import Currency, ExchangeRate, Store, PurchaseCondition
from core.utils.fields import BaseModel


class PurchaseOrder(BaseModel):
    code_po_store = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField()
    supplier = models.ForeignKey(Supplier, related_name="%(app_label)s_%(class)s_supplier")
    currency = models.ForeignKey(Currency, related_name="%(app_label)s_%(class)s_currency")
    applicant = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_user")
    purchase_condition = models.ForeignKey(PurchaseCondition, related_name="%(app_label)s_%(class)s_purchase_condition")
    igv_tax = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    igv_total = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    sub_total = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    total_paid = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    is_authorized = models.BooleanField(default=False)

    def __str__(self):
        return "{0}".format(str(self.date))


class PurchaseOrderDetail(BaseModel):
    purchase_order = models.ForeignKey(
        PurchaseOrder, related_name="%(app_label)s_%(class)s_purchase_order")
    product = models.ForeignKey(
        Product, related_name="%(app_label)s_%(class)s_product")
    description = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.IntegerField(default=0)
    unit_price = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    discount = models.IntegerField(default=0)
    amount_price = models.DecimalField(max_digits=18, decimal_places=2, default=0)

    def __str__(self):
        return "{0}".format(str(self.purchase_order))

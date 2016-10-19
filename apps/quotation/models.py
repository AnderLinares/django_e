from django.db import models

from apps.customer.models import User
from apps.product.models import ProductCategory, ProductSubCategory, Product
from apps.supplier.models import Supplier
from apps.vehicle.models import Vehicle
from core.models import Person, Currency, ExchangeRate
from core.utils.fields import BaseModel


class QuotationMaintenance(BaseModel):
    client = models.ForeignKey(Person, related_name="%(app_label)s_%(class)s_client")
    vehicle = models.ForeignKey(Vehicle, related_name="%(app_label)s_%(class)s_vehicle")
    currency = models.ForeignKey(Currency, blank=True, null=True,
                                 related_name="%(app_label)s_%(class)s_exchange_rate")
    exchange_rate = models.ForeignKey(ExchangeRate, blank=True, null=True,
                                      related_name="%(app_label)s_%(class)s_exchange_rate")
    igv_tax = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    sub_total = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    total_paid = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}".format(str(self.client.first_name), str(self.vehicle.plaque))


class QuotationMaintenanceDetail(BaseModel):
    quotation_maintenance = models.ForeignKey(
        QuotationMaintenance, related_name="%(app_label)s_%(class)s_quotation_maintenance")
    product = models.ForeignKey(
        Product, related_name="%(app_label)s_%(class)s_product")
    description = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    unit_price = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    amount_price = models.DecimalField(max_digits=18, decimal_places=2, default=0)

    def __str__(self):
        return "{0}-{1}".format(str(self.quotation.client), str(self.quotation.vehicle_plaque))


class QuotationStore(BaseModel):
    code_qt_store = models.CharField(max_length=200, null=True, blank=True)
    supplier = models.ForeignKey(Supplier, related_name="%(app_label)s_%(class)s_supplier")
    applicant = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_user")
    date = models.DateField()

    @property
    def get_qt_detail(self):
        qt_detail = QuotationStoreDetail.objects.select_related('quotation_store').filter(pk=self)
        return qt_detail

    def __str__(self):
        return self.supplier


class QuotationStoreDetail(BaseModel):
    quotation_store = models.ForeignKey(
        QuotationStore, related_name="%(app_label)s_%(class)s_quotation_store")
    product = models.ForeignKey(
        Product, related_name="%(app_label)s_%(class)s_product")
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.quotation_store.code_qt_store

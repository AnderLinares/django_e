from django.db import models

from apps.company.models import Subsidiary
from apps.customer.models import UserProfile
from apps.product.models import Product
from apps.taller.models import PurchaseOrderStore
from apps.vehicle.models import Vehicle
from core.models import Store
from core.utils.fields import BaseModel


class ReferenceGuideTallerOrder(BaseModel):
    order_code = models.ForeignKey(
        PurchaseOrderStore, related_name="%(app_label)s_%(class)s_purchase_order_store")
    subsidiary = models.ManyToManyField(
        Subsidiary, related_name="%(app_label)s_%(class)s_subsidiary")
    store_destination = models.ForeignKey(
        Store, related_name="%(app_label)s_%(class)s_store_destination")
    applicant = models.ForeignKey(UserProfile, related_name="%(app_label)s_%(class)s_applicant")
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}".format(str(self.order_code), str(self.subsidiary))


class ReferenceGuideTallerOrderDetail(BaseModel):
    reference = models.ForeignKey(
        ReferenceGuideTallerOrder, related_name="%(app_label)s_%(class)s_purchase_order_store")
    vehicle = models.ForeignKey(Vehicle, related_name="%(app_label)s_%(class)s_vehicle")
    product = models.ForeignKey(
        Product, related_name="%(app_label)s_%(class)s_product")
    description = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=2, default=0)

    def __str__(self):
        return "{0}-{1}".format(str(self.reference), str(self.vehicle))

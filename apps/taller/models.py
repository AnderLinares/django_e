from django.db import models

from apps.company.models import Subsidiary
from apps.customer.models import User
from apps.customer.models import UserProfile
from apps.product.models import (
    ProductCategory, Product)
from apps.vehicle.models import Vehicle
from core import constants as core_constants
from core.models import Person, VehicleInventory, VehicleFuel, LabourCategory, Labour
from core.utils.fields import BaseModel


class ActDeliveryVehicle(BaseModel):
    code_adv_taller = models.CharField(max_length=200, null=True, blank=True)
    service_taller = models.CharField(
        choices=core_constants.TYPE_SERVICES_OPTIONS, max_length=20, null=False, blank=False,
        default=core_constants.CODE_SERVICES_MAINTENANCE)
    type_solicitude_entry = models.CharField(
        choices=core_constants.TYPE_TALLER_SOLICITUDE_OPTIONS, max_length=20, null=False,
        blank=False)
    type_solicitude_exit = models.CharField(
        choices=core_constants.TYPE_TALLER_SOLICITUDE_OPTIONS, max_length=20, null=False,
        blank=False)
    vehicle = models.ForeignKey(Vehicle, related_name="%(app_label)s_%(class)s_vehicle")
    person = models.ForeignKey(Person, related_name="%(app_label)s_%(class)s_person")
    taxi_driver_entry = models.ForeignKey(
        Person, related_name="%(app_label)s_%(class)s_taxi_driver_entry",
        null=True, blank=True, default=None)
    taxi_driver_exit = models.ForeignKey(
        Person, related_name="%(app_label)s_%(class)s_taxi_driver_exit",
        null=True, blank=True, default=None)
    fuel_entry = models.ForeignKey(
        VehicleFuel, related_name="%(app_label)s_%(class)s_fuel_entry",
        null=True, blank=True, default=None)
    fuel_exit = models.ForeignKey(
        VehicleFuel, related_name="%(app_label)s_%(class)s_fuel_exit",
        null=True, blank=True, default=None)
    km_exit = models.PositiveSmallIntegerField(default=0)
    km_entry = models.PositiveSmallIntegerField(default=0)
    date_exit = models.DateField(null=True, blank=True)
    date_entry = models.DateField(null=True, blank=True)
    hour_exit = models.TimeField(default="00:00", null=True, blank=True)
    hour_entry = models.TimeField(default="00:00", null=True, blank=True)
    following_maintenance = models.DateField(null=True, blank=True)
    applicant = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_user")

    def __str__(self):
        return "{0}-{1}".format(str(self.vehicle), str(self.vehicle.plaque))

    @models.permalink
    def get_absolute_url(self):
        return 'ActDeliveryVehicle:detail', [self.pk]


class InventoryDeliveryVehicle(BaseModel):
    act_delivery_vehicle = models.ForeignKey(
        ActDeliveryVehicle, related_name="%(app_label)s_%(class)s_act_delivery_vehicle")
    vehicle_inventory_entry = models.ManyToManyField(
        VehicleInventory, blank=True, related_name="%(app_label)s_%(class)s_vehicle_inventory_entry")
    vehicle_inventory_exit = models.ManyToManyField(
        VehicleInventory, blank=True, related_name="%(app_label)s_%(class)s_vehicle_inventory_exit")

    def get_inventory_entry_list(self):
        return ", ".join([p.name for p in self.vehicle_inventory_entry.all()])

    def get_inventory_exit_list(self):
        return ", ".join([p.name for p in self.vehicle_inventory_exit.all()])

    def __str__(self):
        return "{0}-{1}".format(str(self.act_delivery_vehicle), str(self.act_delivery_vehicle.vehicle.plaque))


class ObservationDeliveryVehicle(BaseModel):
    act_delivery_vehicle = models.ForeignKey(
        ActDeliveryVehicle, related_name="%(app_label)s_%(class)s_act_delivery_vehicle")
    observation_inspection = models.TextField(blank=True, null=True)
    observation_evaluation = models.TextField(blank=True, null=True)
    observation_correction = models.TextField(blank=True, null=True)
    observation_conclusion = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{0}-{1}".format(str(self.act_delivery_vehicle), str(self.act_delivery_vehicle.vehicle.plaque))


class WorkAssignment(BaseModel):
    code_wka_maintenance = models.CharField(max_length=200, null=True, blank=True)
    vehicle = models.ForeignKey(Vehicle, related_name="%(app_label)s_%(class)s_vehicle")
    client = models.ForeignKey(Person, related_name="%(app_label)s_%(class)s_vehicle")
    applicant = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_user")

    def get_count_work_assignment(self):
        return WorkAssignmentDetail.objects.filter(
            work_assignment=self.pk
        ).prefetch_related('work_assignment').count()

    def get_status_supervisor(self):
        return WorkAssignmentDetail.objects.filter(
            work_assignment=self.pk, is_finished_supervisor=True
        ).prefetch_related('work_assignment').count()

    def __str__(self):
        return self.vehicle.plaque


class WorkAssignmentDetail(BaseModel):
    work_assignment = models.ForeignKey(WorkAssignment, related_name="%(app_label)s_%(class)s_work_assignment")
    labour_category = models.ForeignKey(LabourCategory, related_name="%(app_label)s_%(class)s_labour_category")
    labour = models.ForeignKey(Labour, related_name="%(app_label)s_%(class)s_labour")
    description_labour = models.TextField(blank=True, null=True)
    mechanic = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_mechanic")
    description_mechanic = models.TextField(blank=True, null=True)
    is_finished_mechanic = models.BooleanField(default=False)
    is_finished_supervisor = models.BooleanField(default=False)

    @models.permalink
    def get_absolute_mechanic_url(self):
        return 'MechanicAssignment:detail', [self.id]

    @models.permalink
    def get_update_observation_url(self):
        return 'MechanicAssignment:observation-update', [self.id]

    @models.permalink
    def get_update_store_url(self):
        return 'MechanicAssignment:store-update', [self.id]

    def __str__(self):
        return self.work_assignment.vehicle.plaque


class WorkAssignmentStore(BaseModel):
    work_assignment = models.ForeignKey(WorkAssignmentDetail, related_name="%(app_label)s_%(class)s_work_assignment")
    product = models.ForeignKey(Product, related_name="%(app_label)s_%(class)s_product")
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.work_assignment.vehicle.work_assignment.vehicle.plaque


class RequisitionStore(BaseModel):
    code_spt = models.CharField(max_length=200, null=True, blank=True)
    client = models.ForeignKey(Person, related_name="%(app_label)s_%(class)s_client")
    applicant = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_user")
    status_requisition = models.CharField(
        max_length=20, default=core_constants.CODE_TALLER_REQUISITION_PENDING,
        choices=core_constants.TYPE_TALLER_REQUISITION_OPTIONS)

    @models.permalink
    def get_absolute_detail_url(self):
        return 'RequisitionStore:detail', [self.id]

    def __str__(self):
        return "{0}-{1}".format(self.code_spt, self.status_requisition)


class RequisitionStoreDetail(BaseModel):
    requisition_store = models.ForeignKey(RequisitionStore, related_name="%(app_label)s_%(class)s_requisition_store")
    vehicle = models.ForeignKey(Vehicle, related_name="%(app_label)s_%(class)s_vehicle")
    product_category = models.ForeignKey(ProductCategory, related_name="%(app_label)s_%(class)s_product_category")
    product = models.ForeignKey(Product, related_name="%(app_label)s_%(class)s_product")
    quantity = models.PositiveSmallIntegerField(default=1)
    is_urgent = models.BooleanField(default=False)
    observation = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.requisition_store.code_spt

from django.db import models

from apps.client.models import Person
from apps.employee.models import Employee
from core.models import Subsidiary, Currency, ExchangeRate
from core.utils.fields import BaseModel
from .constants import *


class Brand(BaseModel):
    """ model Brand(marca) """
    name = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        unique_together = ['name']

    def __str__(self):
        return self.name


class TypeTransport(BaseModel):
    """ model TypeVehicle(tipo vehiculo) """
    name = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        unique_together = ['name']

    def __str__(self):
        return self.name


# class TypeInspectionCheckList(BaseModel):
#     """ model TypeInspectionCheckList(tipo inspeccion) """
#     name = models.CharField(max_length=200, null=True, blank=True)
#
#     class Meta:
#         unique_together = ['name']
#
#     def __str__(self):
#         return self.name


class TransportInventory(BaseModel):
    """ model TypeInventoryCheckList(tipo checklist) """
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class ServiceCheckList(BaseModel):
    """ model ServiceCheckList(tipo checklist) """
    name = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        unique_together = ['name']

    def __str__(self):
        return self.name


class SolicitudeCheckList(BaseModel):
    """ model ServiceSolicitudeCheckList(tipo checklist)
        ENTRY-DEPARTURE-LIGHTWEIGHT
    """
    name = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        unique_together = ['name']

    def __str__(self):
        return self.name


class TypeFuel(BaseModel):
    """ model TypeVehicle(tipo vehiculo) """
    name = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        unique_together = ['name']

    def __str__(self):
        return self.name


class TypeCheckList(BaseModel):
    """ model TypeCheckList(tipo checklist) """
    service_checklist = models.ForeignKey(
        ServiceCheckList, related_name="%(app_label)s_%(class)s_type_service_checklist")
    type_transport = models.ForeignKey(
        TypeTransport, related_name="%(app_label)s_%(class)s_type_transport")
    solicitude_checklist = models.ForeignKey(
        SolicitudeCheckList, related_name="%(app_label)s_%(class)s_solicitude_checklist")

    class Meta:
        unique_together = ['service_checklist', 'type_transport', 'solicitude_checklist']

    def __str__(self):
        return "{0}-{1}-{2}".format(str(self.service_checklist),
                                    str(self.type_transport),
                                    str(self.solicitude_checklist))


class TypeLabour(BaseModel):
    """ model TypeJob(tipo trabajo) """
    name = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        unique_together = ['name']

    def __str__(self):
        return self.name


class Labour(BaseModel):
    """ model Labour(labores) """
    type_labour = models.ForeignKey(TypeLabour, related_name="%(app_label)s_%(class)s_type_labour")
    name = models.CharField(max_length=200, null=True, blank=True)
    cost_price = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    sale_price = models.DecimalField(max_digits=18, decimal_places=2, default=0)

    class Meta:
        unique_together = ["type_labour", "name"]

    def __str__(self):
        return self.name


class Vehicle(BaseModel):
    """ model Vehicle(vehiculo) """
    type_transport = models.ForeignKey(TypeTransport, related_name="%(app_label)s_%(class)s_type_transport")
    brand = models.ForeignKey(Brand, related_name="%(app_label)s_%(class)s_brand")
    subsidiary = models.ForeignKey(Subsidiary, related_name="%(app_label)s_%(class)s_subsidiary")
    plaque = models.CharField(max_length=200, null=True, blank=True)
    model = models.CharField(max_length=200, null=True, blank=True)
    year_car = models.PositiveSmallIntegerField(null=True, blank=True)
    vin = models.CharField(max_length=100, null=True, blank=True)
    color = models.CharField(max_length=200, null=True, blank=True)
    serie_motor = models.CharField(max_length=200, null=True, blank=True)
    soat = models.CharField(max_length=100, blank=True, null=True)
    expiration_soat = models.DateTimeField(blank=True, null=True)
    poliza = models.CharField(max_length=100, blank=True, null=True)
    expiration_poliza = models.DateTimeField(blank=True, null=True)
    technical_review = models.CharField(max_length=100, blank=True, null=True)
    expiration_technical_review = models.DateTimeField(blank=True, null=True)
    opacity_test = models.CharField(max_length=100, blank=True, null=True)
    expiration_opacity_test = models.DateTimeField(blank=True, null=True, )
    farenet_test = models.CharField(max_length=100, blank=True, null=True)
    expiration_farenet_test = models.DateTimeField(blank=True, null=True)
    is_flotilla = models.BooleanField(default=False)

    class Meta:
        unique_together = ["subsidiary", "plaque"]

    def __str__(self):
        return "{0}-{1}-{2}".format(
            str(self.type_transport.name), str(self.brand.name), str(self.subsidiary.name)
        )


class Quotation(BaseModel):
    """ model Quotation(Cotizacion) """
    client = models.ForeignKey(Person, related_name="%(app_label)s_%(class)s_person")
    vehicle = models.ForeignKey(Vehicle, related_name="%(app_label)s_%(class)s_vehicle")
    labour = models.ForeignKey(Labour, related_name="%(app_label)s_%(class)s_labour")
    exchange_rate = models.ForeignKey(ExchangeRate, blank=True, null=True,
                                      related_name="%(app_label)s_%(class)s_exchange_rate")
    igv_tax = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    sub_total = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    total_paid = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    current_date = models.DateField()

    def __str__(self):
        return "{0}-{1}".format(str(self.client.first_name), str(self.vehicle.plaque))


class QuotationDetail(BaseModel):
    """ model QuotationDetail(cotizacion detalle) """
    quotation = models.ForeignKey(Quotation, related_name="%(app_label)s_%(class)s_quotation")
    description = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    unit_price = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    amount_price = models.DecimalField(max_digits=18, decimal_places=2, default=0)

    def __str__(self):
        return "{0}-{1}".format(str(self.quotation.client), str(self.quotation.vehicle))


class Report(BaseModel):
    client = models.ForeignKey(Person, related_name="%(app_label)s_%(class)s_client")
    vehicle = models.ForeignKey(Vehicle, related_name="%(app_label)s_%(class)s_vehicle")
    subsidiary = models.ForeignKey(Subsidiary, related_name="%(app_label)s_%(class)s_subsidiary")
    current_date = models.DateTimeField(blank=True, null=True)
    observation = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{0}".format(str(self.client))


class ReportDocument(BaseModel):
    report = models.ForeignKey(Report, related_name="%(app_label)s_%(class)s_report")
    file_image = models.FileField(upload_to='report/%Y-%m-%d/', blank=True, null=True)

    def __str__(self):
        return "{0}".format(str(self.report))


class CheckList(BaseModel):
    client = models.ForeignKey(Person, related_name="%(app_label)s_%(class)s_client")
    vehicle = models.ForeignKey(Vehicle, related_name="%(app_label)s_%(class)s_vehicle")
    subsidiary = models.ForeignKey(Subsidiary, related_name="%(app_label)s_%(class)s_subsidiary")
    destination = models.CharField(max_length=200, blank=True, null=True)
    number_billing = models.CharField(max_length=45, blank=True, null=True)
    number_contract = models.CharField(max_length=45, blank=True, null=True)
    status_checklist = models.CharField(
        max_length=10, blank=True, null=True, default=CODE_STATUS_CHECKLIST_PENDING,
        choices=STATUS_CHECKLIST_DETAIL_OPTIONS)

    class Meta:
        unique_together = ['number_billing', 'subsidiary']

    def __str__(self):
        return "{0}-{1}".format(str(self.client), str(self.vehicle))


class CheckListDetail(BaseModel):
    checklist = models.ForeignKey(CheckList, related_name="%(app_label)s_%(class)s_checklist")
    service_checklist = models.ForeignKey(ServiceCheckList, related_name="%(app_label)s_%(class)s_service_checklist")
    type_transport = models.ForeignKey(TypeTransport, related_name="%(app_label)s_%(class)s_type_transport")
    type_checklist = models.CharField(max_length=10, blank=True, null=True, choices=TYPE_CHECKLIST_SOLICITUDE_OPTIONS)
    taxi_driver = models.CharField(max_length=200, blank=True, null=True)
    date_initial = models.DateTimeField(blank=True, null=True)
    hour_initial = models.TimeField(blank=True, null=True)
    fuel_initial = models.CharField(max_length=200, blank=True, null=True, choices=STATUS_CCODE_FUEL_DETAIL_OPTIONS)
    km_initial = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, default=0)
    kms_next_maintenance = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, default=0)
    observation = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{0}-{1}".format(str(self.service_checklist), str(self.type_checklist))


class InventoryCheckList(BaseModel):
    checklist_detail = models.ForeignKey(
        CheckListDetail, related_name="%(app_label)s_%(class)s_checklist_detail")
    inventory_checklist = models.ForeignKey(
        TransportInventory, related_name="%(app_label)s_%(class)s_type_inventory_checklist")

    class Meta:
        unique_together = ["checklist_detail", "inventory_checklist"]

    def __str__(self):
        return "{0}-[1]".format(str(self.checklist_detail), str(self.inventory_checklist))


class PhotoCheckList(BaseModel):
    checklist_detail = models.ForeignKey(
        CheckListDetail, related_name="%(app_label)s_%(class)s_checklist_detail")
    photo_checklist = models.FileField(upload_to='photo_checklist/%Y-%m-%d/', blank=True, null=True)

    def __str__(self):
        return "{0}-{1}".format(str(self.checklist_detail), str(self.photo_checklist))


class LabourCheckList(BaseModel):
    checklist_detail = models.ForeignKey(
        CheckListDetail, related_name="%(app_label)s_%(class)s_checklist_detail")
    labour = models.ForeignKey(
        Labour, related_name="%(app_label)s_%(class)s_labour")
    employee = models.ForeignKey(Employee, related_name="%(app_label)s_%(class)s_employee")
    description = models.TextField(blank=True, null=True)
    status_labour = models.CharField(
        max_length=10, blank=True, null=True, default=CODE_STATUS_CHECKLIST_PENDING,
        choices=STATUS_CHECKLIST_DETAIL_OPTIONS)

    class Meta:
        unique_together = ["checklist_detail", "labour", "employee"]

    def __str__(self):
        return "{0}-{1}".format(str(self.checklist_detail), str(self.labour))


class LabourEmployeeCheckList(BaseModel):
    labour_checklist = models.ForeignKey(
        LabourCheckList, related_name="%(app_label)s_%(class)s_labour_checklist")
    task = models.CharField(max_length=200, blank=True, null=True)
    is_status = models.BooleanField(default=False)

    def __str__(self):
        return "{0}".format(str(self.labour_checklist))


class SupervisionLabourCheckList(BaseModel):
    checklist_detail = models.ForeignKey(
        CheckListDetail, related_name="%(app_label)s_%(class)s_checklist_detail")
    description = models.TextField(blank=True, null=True)
    job_rating = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return "{0}".format(str(self.checklist_detail))



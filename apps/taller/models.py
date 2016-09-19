from django.db import models

from apps.client.models import Person
from apps.employee.models import Employee
from core.models import Subsidiary, Currency, ExchangeRate
from core.utils.fields import BaseModel
from .constants import (
    STATUS_VEHICLE_OPTIONS, TYPE_COMBUSTIBLE_OPTIONS, TYPE_ORDER_OPTIONS,
    STATUS_GLOBAL_OPTION, STATUS_ORDER_DETAIL_OPTIONS,
    CODE_STATUS_AVAILABLE)


class Brand(BaseModel):
    """ model Brand(marca) """
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class TypeJob(BaseModel):
    """ model TypeJob(tipo trabajo) """
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class TypeCheckList(BaseModel):
    """ model TypeCheckList(tipo checklist) """
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class TypeVehicle(BaseModel):
    """ model TypeVehicle(tipo vehiculo) """
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class TypeFuel(BaseModel):
    """ model TypeVehicle(tipo vehiculo) """
    type_fuel = models.CharField(max_length=100, choices=TYPE_COMBUSTIBLE_OPTIONS)
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Labour(BaseModel):
    """ model Labour(labores) """
    type_job = models.ForeignKey(TypeJob, related_name="%(app_label)s_%(class)s_type_job")
    name = models.CharField(max_length=200, null=True, blank=True)
    cost_price = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    sale_price = models.DecimalField(max_digits=18, decimal_places=2, default=0)

    def __str__(self):
        return self.type_job.name


class Vehicle(BaseModel):
    """ model Vehicle(vehiculo) """
    type_vehicle = models.ForeignKey(TypeVehicle, related_name="%(app_label)s_%(class)s_type_vehicle")
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
    status_vehicle = models.CharField(max_length=10, choices=STATUS_VEHICLE_OPTIONS,
                                      default=CODE_STATUS_AVAILABLE)

    def __str__(self):
        return "{0}-{1}-{2}".format(
            str(self.type_vehicle.name), str(self.brand.name), str(self.subsidiary.name)
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
        return "{0}-{1}".format(str(self.cotization.client), str(self.cotization.vehicle))


class Order(BaseModel):
    client = models.ForeignKey(Person, related_name="%(app_label)s_%(class)s_client")
    vehicle = models.ForeignKey(Vehicle, related_name="%(app_label)s_%(class)s_vehicle")
    type_checklist = models.ForeignKey(TypeCheckList, related_name="%(app_label)s_%(class)s_type_checklist")
    subsidiary = models.ForeignKey(Subsidiary, related_name="%(app_label)s_%(class)s_subsidiary")
    number = models.PositiveIntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    taxi_driver = models.CharField(max_length=200, blank=True, null=True)
    destination = models.CharField(max_length=200, blank=True, null=True)
    date_arrival = models.DateTimeField(blank=True, null=True)
    hour_arrival = models.TimeField(blank=True, null=True)
    fuel_arrival = models.PositiveSmallIntegerField(blank=True, null=True)
    unit_number_arrival = models.CharField(max_length=45, blank=True, null=True)
    km_arrival = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    date_exit = models.DateTimeField(blank=True, null=True)
    hour_exit = models.TimeField(blank=True, null=True)
    fuel_exit = models.PositiveSmallIntegerField(blank=True, null=True)
    unit_number_exit = models.CharField(max_length=45, blank=True, null=True)
    km_exit = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, default=0)
    kms_next_maintenance = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, default=0)
    number_billing = models.PositiveIntegerField(blank=True, null=True)
    number_contract = models.CharField(max_length=45, blank=True, null=True)
    status_order = models.CharField(max_length=10, choices=STATUS_GLOBAL_OPTION)
    type_order = models.CharField(max_length=10, choices=TYPE_ORDER_OPTIONS)
    observation_delivery = models.TextField(blank=True, null=True)
    observation_refund = models.TextField(blank=True, null=True)
    observation_inspection = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{0}-{1}".format(str(self.client), str(self.vehicle))


class OrderDetail(BaseModel):
    order = models.ForeignKey(Order, related_name="%(app_label)s_%(class)s_order")
    type_vehicle = models.ForeignKey(TypeVehicle, related_name="%(app_label)s_%(class)s_type_vehicle")
    labour = models.ForeignKey(Labour, related_name="%(app_label)s_%(class)s_labour")
    employee = models.ForeignKey(Employee, related_name="%(app_label)s_%(class)s_employee")
    status_order = models.CharField(max_length=3, choices=STATUS_ORDER_DETAIL_OPTIONS)

    def __str__(self):
        return "{0}".format(str(self.order))


class OrderDocument(BaseModel):
    order = models.ForeignKey(Order, related_name="%(app_label)s_%(class)s_order")
    file_image = models.FileField(upload_to='checklists/%Y/%m/%d/')

    def __str__(self):
        return "{0}".format(str(self.order))


class OrderSupervision(BaseModel):
    order_detail = models.ForeignKey(OrderDetail, related_name="%(app_label)s_%(class)s_order_detail")
    employee = models.ForeignKey(Employee, related_name="%(app_label)s_%(class)s_employee")
    observation = models.TextField()
    job_rating = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return "{0}".format(str(self.order_detail))


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
    file_image = models.FileField(upload_to='report/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return "{0}".format(str(self.report))

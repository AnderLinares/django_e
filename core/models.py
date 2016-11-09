from django.db import models

from core import constants as core_constants
from core.utils.fields import BaseModel, BaseModel2


class Currency(BaseModel):
    sk = models.CharField(max_length=30, blank=True, null=True)
    code = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    is_fund = models.BooleanField(default=False)
    is_complimentary = models.BooleanField(default=False)
    is_metal = models.BooleanField(default=False)

    class Meta:
        unique_together = ["sk", "code", "name"]

    def __str__(self):
        return self.name


class ExchangeRate(BaseModel):
    currency = models.ForeignKey(Currency,
                                 related_name="%(app_label)s_%(class)s_currency")
    exchange_rate = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(blank=True, null=True, default=None)

    def __str__(self):
        return "{0}-{1}".format(str(self.currency.name), str(self.exchange_rate))


class HandWorkCategory(BaseModel):
    name = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        unique_together = ["name"]

    def __str__(self):
        return self.name


class HandWork(BaseModel):
    handwork_category = models.ForeignKey(HandWorkCategory, related_name="%(app_label)s_%(class)s_handwork_category")
    name = models.CharField(max_length=200, null=True, blank=True)
    currency = models.ForeignKey(Currency, related_name="%(app_label)s_%(class)s_currency")
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, null=True, blank=True)

    class Meta:
        unique_together = ["handwork_category", "name"]

    def __str__(self):
        return self.name


class LabourCategory(BaseModel):
    name = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        unique_together = ["name"]

    def __str__(self):
        return self.name


class Labour(BaseModel):
    labour_category = models.ForeignKey(LabourCategory, related_name="%(app_label)s_%(class)s_labour_category")
    name = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        unique_together = ["labour_category", "name"]

    def __str__(self):
        return self.name


class UnitMeasurement(BaseModel):
    type_measurement = models.CharField(max_length=20, choices=core_constants.TYPE_UNIT_MEASUREMENT_OPTIONS)
    name = models.CharField(max_length=120, null=False, blank=False)
    symbol = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        unique_together = ["type_measurement", "name"]

    def __str__(self):
        return "{0}-{1}".format(str(self.get_type_measurement_display()), str(self.name))


class VehicleEnrollment(BaseModel):
    year = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        unique_together = ["year"]

    def __str__(self):
        return self.year


class VehicleBrand(BaseModel):
    """ model Brand(marca) """
    name = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        unique_together = ["name"]

    def __str__(self):
        return self.name


class VehicleModel(BaseModel):
    """ model Model(marca) """
    brand = models.ForeignKey(VehicleBrand, related_name="%(app_label)s_%(class)s_brand")
    name = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        unique_together = ["brand", "name"]

    def __str__(self):
        return self.name


class VehicleFuel(BaseModel):
    unit_transport = models.ForeignKey(
        UnitMeasurement, related_name="%(app_label)s_%(class)s_type_transport",
        limit_choices_to={'type_measurement__in': [core_constants.CODE_MEASUREMENT_PURCHASE_LIQUID_UNIT]})
    name = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        unique_together = ["name", "unit_transport"]

    def __str__(self):
        return self.name


class PurchaseCondition(BaseModel):
    name = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        unique_together = ["name"]

    def __str__(self):
        return self.name


class TaxConfiguration(BaseModel):
    name = models.CharField(max_length=200, null=True, blank=True)
    value = models.DecimalField(max_digits=18, decimal_places=2, default=0)

    class Meta:
        unique_together = ["name"]

    @staticmethod
    def get_igv_value():
        tax = TaxConfiguration.objects.get(name="IGV")
        return tax.value

    def __str__(self):
        return self.name


class ProductBrand(BaseModel):
    """ model Brand(marca) """
    name = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        unique_together = ["name"]

    def __str__(self):
        return self.name


class ProductModel(BaseModel):
    """ model Model(marca) """
    brand = models.ForeignKey(ProductBrand, related_name="%(app_label)s_%(class)s_brand")
    name = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        unique_together = ["brand", "name"]

    def __str__(self):
        return self.name


class TypeContributionSystem(BaseModel):
    type_contribution = models.CharField(max_length=20, choices=core_constants.TYPE_CONTRIBUTION_SYSTEM__OPTIONS)
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class ContributionSystem(BaseModel):
    type_contribution = models.ForeignKey(TypeContributionSystem,
                                          related_name="%(app_label)s_%(class)s_type_contribution")
    percentage = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    number_account = models.CharField(max_length=20, null=True, blank=True)
    plame = models.CharField(max_length=20, null=True, blank=True)
    percentage_bonus = models.DecimalField(max_digits=8, decimal_places=2, default=0, null=True)
    top = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, default=0)

    def __str__(self):
        return self.type_contribution.name


class Bank(BaseModel):
    name = models.CharField(max_length=120, null=False, blank=False)

    def __str__(self):
        return self.name


class Specialty(BaseModel):
    name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name


class VehicleInventory(BaseModel):
    name = models.CharField(max_length=200, null=False, blank=False)

    class Meta:
        unique_together = ["name"]

    def __str__(self):
        return self.name


class Service(BaseModel):
    name = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        unique_together = ["name"]

    def __str__(self):
        return self.name


class Store(BaseModel):
    name = models.CharField(max_length=100, null=False, blank=False)
    is_principal = models.BooleanField(default=False)

    class Meta:
        unique_together = ["name"]

    def __str__(self):
        return self.name


class Person(BaseModel):
    """ model Person(persona) """
    first_name = models.CharField(max_length=100, blank=True,
                                  null=True, unique=False)
    last_name = models.CharField(max_length=100, blank=True,
                                 null=True, unique=False)
    email = models.EmailField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    home_phone = models.CharField(max_length=50, blank=True, null=True)
    mobile_phone = models.CharField(max_length=50, blank=True, null=True)
    document_type = models.CharField(
        max_length=20, null=True, blank=True,
        choices=core_constants.SELECT_DEFAULT + core_constants.TYPE_IDENTITY_DOCUMENT_OPTIONS)
    document_number = models.CharField(max_length=20, null=True, blank=True)
    person_tribute = models.CharField(
        max_length=20, null=True, blank=True,
        choices=core_constants.SELECT_DEFAULT + core_constants.TRIBUTE_PERSON_OPTIONS)
    is_client = models.BooleanField(default=False)
    is_taxi_driver = models.BooleanField(default=False)

    class Meta:
        unique_together = ["email"]

    def __str__(self):
        return "{0}-{1}".format(self.first_name, self.get_person_tribute_display())


class ConsultService(BaseModel):
    name = models.CharField(max_length=100, null=False, blank=False)
    url_service = models.URLField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = ["name", "url_service"]

    def __str__(self):
        return self.name

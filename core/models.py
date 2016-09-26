from django.contrib.auth.models import (
    Group
)
from django.db import models

from core import constants as core_constants
from core.utils.fields import BaseModel, BaseModel2
from .custom_upload import upload_location_organization


class Module(BaseModel2):
    """ model module(modulo) """
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Team(BaseModel2):
    """ model team(grupo) """
    group = models.OneToOneField(
        Group, unique=True, db_index=True,
        related_name="%(app_label)s_%(class)s_group",
        on_delete=False)
    module = models.ForeignKey(Module, related_name="%(app_label)s_%(class)s_module")

    class Meta:
        unique_together = ['group', 'module']
        ordering = ['date_created']

    def __str__(self):
        return "{0}-{1}".format(str(self.group.name), str(self.module.name))


class Currency(BaseModel):
    sk = models.CharField(max_length=30, blank=True, null=True)
    code = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    is_fund = models.BooleanField(default=False)
    is_complimentary = models.BooleanField(default=False)
    is_metal = models.BooleanField(default=False)

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


class Zone(BaseModel):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Country(BaseModel):
    zone = models.ForeignKey(Zone, related_name="%(app_label)s_%(class)s_zone")
    name = models.CharField(max_length=50, null=True, blank=True)
    code = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    iso_code = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class State(BaseModel):
    zone = models.ForeignKey(Zone, related_name="%(app_label)s_%(class)s_zone")
    country = models.ForeignKey(Country,
                                related_name="%(app_label)s_%(class)s_country")
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Organization(BaseModel):
    """ model Organization(organizacion) """
    name = models.CharField(max_length=200, blank=True, null=True)
    reason_social = models.CharField(max_length=100, blank=True, null=True)
    initial_exercise = models.DateTimeField(blank=True, null=True)
    final_exercise = models.DateTimeField(blank=True, null=True)
    nit = models.CharField(max_length=20, blank=True, null=True)
    legal_representative = models.CharField(max_length=100, blank=True, null=True)
    accountant = models.CharField(max_length=100, blank=True, null=True)
    register_accountant = models.PositiveIntegerField(default=0)
    address = models.CharField(max_length=200, blank=True, null=True)
    logo_url = models.ImageField(upload_to="organization/", blank=True, null=True)
    primary_currency = models.ForeignKey(Currency,
                                         related_name="%(app_label)s_%(class)s_currency")
    phone = models.CharField(max_length=50, blank=True, null=True)
    mobile_phone = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class Subsidiary(BaseModel):
    """ model Subsidiary(surcusal) """
    organization = models.ForeignKey(Organization,
                                     related_name="%(app_label)s_%(class)s_organization")
    name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    mobile_phone = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class TypeContributionSystem(BaseModel):
    type_contribution = models.CharField(max_length=10, choices=core_constants.TYPE_CONTRIBUTION_SYSTEM__OPTIONS)
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class ContributionSystem(BaseModel):
    type_contribution = models.ForeignKey(TypeContributionSystem,
                                          related_name="%(app_label)s_%(class)s_type_contribution")
    percentage = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    number_account = models.CharField(max_length=20, null=True, blank=True)
    plame = models.CharField(max_length=12, null=True, blank=True)
    percentage_bonus = models.DecimalField(max_digits=8, decimal_places=4, default=0, null=True)
    top = models.DecimalField(max_digits=8, decimal_places=4, null=True, blank=True, default=0)

    def __str__(self):
        return self.type_contribution.name


class Bank(BaseModel):
    name = models.CharField(max_length=120, null=False, blank=False)

    def __str__(self):
        return self.name


class Specialty(BaseModel):
    name = models.CharField(max_length=120, null=False, blank=False)

    def __str__(self):
        return self.name


class Correlative(BaseModel):
    subsidiary = models.ForeignKey(Subsidiary,
                                   related_name="%(app_label)s_%(class)s_subsidiary")
    type_correlative = models.CharField(max_length=10, choices=core_constants.TYPE_CORRELATIVE_OPTIONS)
    prefix = models.CharField(max_length=20, null=True, blank=True)
    postfix = models.CharField(max_length=20, null=True, blank=True)
    format = models.CharField(max_length=20, null=True, blank=True)
    initial = models.IntegerField(default=1)
    increment = models.IntegerField(default=1)
    final = models.IntegerField(null=True, blank=True)
    actual = models.IntegerField(default=0)

    @staticmethod
    def get_current_correlative_checklist(subsidiary, type_correlative):
        correlative = Correlative.objects.get(subsidiary=subsidiary, type_correlative=type_correlative)
        actual_correlative = correlative.actual + correlative.increment
        current_format = "{0}-{1}".format(str(correlative.prefix), str(correlative.format))
        exact_number = "{0}{1}".format(current_format.strip(), str(actual_correlative))
        post_correlative = int(actual_correlative) + int(correlative.increment)
        result = dict(actual_correlative=actual_correlative, exact_number=exact_number,
                      current_format=current_format, post_correlative=post_correlative)
        return result

    @staticmethod
    def get_correlative_update(subsidiary, type_correlative, actual_number):
        correlative = Correlative.objects.get(subsidiary=subsidiary, type_correlative=type_correlative)
        correlative.actual = actual_number
        correlative.save()

    def __str__(self):
        return "{0}-{1}-{2}".format(str(self.prefix), str(self.postfix), str(self.actual))


class UnitMeasurement(BaseModel):
    type_measurement = models.CharField(max_length=10, choices=core_constants.TYPE_UNIT_MEASUREMENT_OPTIONS)
    name = models.CharField(max_length=120, null=False, blank=False)
    symbol = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return "{0}-{1}".format(str(self.get_type_measurement_display()), str(self.name))

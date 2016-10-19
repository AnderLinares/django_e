from django.db import models

from apps.billing.models import TypeDocument
from core import constants as core_constants
from core.models import Store
from core.utils.fields import BaseModel


class Organization(BaseModel):
    """ model Organization(organizacion) """
    business_name = models.CharField(max_length=100, blank=True, null=True)
    document_type = models.CharField(
        max_length=20, null=False, blank=False,
        choices=[core_constants.SIS_DOCUMENT_RUC_STRING])
    document_number = models.CharField(max_length=20, null=False, blank=False)
    address = models.CharField(max_length=200, blank=True, null=True)
    logo_url = models.ImageField(upload_to="organization/", blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    mobile_phone = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        unique_together = ["business_name", "document_number"]

    def __str__(self):
        return self.business_name


class Subsidiary(BaseModel):
    """ model Subsidiary(surcusal) """
    organization = models.ForeignKey(Organization,
                                     related_name="%(app_label)s_%(class)s_organization")
    subsidiary_name = models.CharField(max_length=100, blank=True, null=True)
    store_local = models.ForeignKey(
        Store, related_name="%(app_label)s_%(class)s_store_local")
    representative = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    mobile_phone = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        unique_together = ["organization", "store_local"]

    def __str__(self):
        return self.subsidiary_name


class Correlative(BaseModel):
    organization = models.ForeignKey(Organization,
                                     related_name="%(app_label)s_%(class)s_organization")
    subsidiary = models.ForeignKey(Subsidiary,
                                   related_name="%(app_label)s_%(class)s_subsidiary")
    type_document = models.ForeignKey(TypeDocument,
                                      related_name="%(app_label)s_%(class)s_type_document")
    prefix = models.CharField(max_length=20, null=True, blank=True)
    postfix = models.CharField(max_length=20, null=True, blank=True)
    format = models.CharField(max_length=20, null=True, blank=True)
    initial = models.IntegerField(default=1)
    increment = models.IntegerField(default=1)
    final = models.IntegerField(null=True, blank=True)
    actual = models.IntegerField(default=0)

    class Meta:
        unique_together = ["organization", "subsidiary", "type_document"]

    @staticmethod
    def get_current_document(abbreviation, subsidiary):
        """
        :param abbreviation: String CO, FA, BO, GR, ND, NC
        :param subsidiary: object subsidiary
        :return: last correlative
        """
        type_document = TypeDocument.objects.get(abbreviation=abbreviation)
        current = Correlative.objects.get(type_document=type_document, subsidiary=subsidiary)
        current_correlative = current.actual
        current_aggregate = current.actual + current.increment
        current_aggregate_format = "{0}-{1}-{2}{3}".format(
            str(current.prefix), str(current.postfix), str(current.format), str(current_aggregate))
        correlative_dict = dict(current_correlative=current_correlative,
                                current_aggregate=current_aggregate,
                                current_aggregate_format=current_aggregate_format)
        return correlative_dict

    @staticmethod
    def save_current_document(abbreviation, subsidiary):
        """
        :param abbreviation: String CO, FA, BO, GR, ND, NC
        :param subsidiary: object subsidiary
        :return: update correlative
        """
        type_document = TypeDocument.objects.get(abbreviation=abbreviation)
        current = Correlative.objects.get(type_document=type_document, subsidiary=subsidiary)
        current.actual = current.actual + current.increment
        current.save()
        return current

    def __str__(self):
        return "{0}-{1}-{2}-{3}".format(str(self.prefix), str(self.postfix), str(self.actual), str(self.subsidiary))

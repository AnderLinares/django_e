from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import Subsidiary, Module
from core import constants as core_constants
from core.utils.fields import BaseModel


class Person(BaseModel):
    """ model Person(persona) """
    module = models.ForeignKey(Module, blank=True, null=True,
                               related_name="%(app_label)s_%(class)s_module")
    first_name = models.CharField(_('first name'), max_length=100, blank=True,
                                  null=True, unique=False)
    last_name = models.CharField(_('last name'), max_length=100, blank=True,
                                 null=True, unique=False)
    email = models.EmailField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    home_phone = models.CharField(max_length=50, blank=True, null=True)
    mobile_phone = models.CharField(max_length=50, blank=True, null=True)
    subsidiary = models.ForeignKey(Subsidiary, default='', blank=True, null=True,
                                   related_name="%(app_label)s_%(class)s_subsidiary")
    document_type = models.CharField(
        max_length=20, null=True, blank=True,
        choices=core_constants.SELECT_DEFAULT + core_constants.TYPE_IDENTITY_DOCUMENT_OPTIONS)
    document_number = models.CharField(max_length=20, null=True, blank=True)
    person_type = models.CharField(
        max_length=20, null=True, blank=True,
        choices=core_constants.SELECT_DEFAULT + core_constants.TYPE_PERSON_OPTIONS)

    def __str__(self):
        return "{0}-{1}".format(self.first_name, self.get_person_type_display())



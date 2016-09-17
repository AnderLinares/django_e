from django.db import models
from django.utils.translation import ugettext_lazy as _

from core import constants as core_constants
from core.models import ContributionSystem, TypeContributionSystem, Bank, Specialty, Subsidiary


class Employee(models.Model):
    subsidiary = models.ForeignKey(Subsidiary, related_name="%(app_label)s_%(class)s_subsidiary")
    document_type = models.CharField(
        max_length=20, null=True, blank=True,
        choices=core_constants.SELECT_DEFAULT + core_constants.TYPE_IDENTITY_DOCUMENT_OPTIONS)
    document_number = models.CharField(max_length=20, null=True, blank=True)
    first_name = models.CharField(_('first name'), max_length=100, blank=True,
                                  null=True, unique=False)
    last_name = models.CharField(_('last name'), max_length=100, blank=True,
                                 null=True, unique=False)
    home_phone = models.CharField(max_length=50, blank=True, null=True)
    mobile_phone = models.CharField(max_length=50, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    civil_status = models.CharField(max_length=10, choices=core_constants.TYPE_CIVIL_STATUS_OPTIONS)
    gender = models.CharField(max_length=10, choices=core_constants.TYPE_GENDER_OPTIONS)
    stature = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    peso = models.IntegerField(blank=True, null=True)
    type_brevete = models.CharField(max_length=10, choices=core_constants.TYPE_BREVETE_OPTIONS)
    number_license_brevete = models.CharField(max_length=20, blank=True, null=True)
    type_pension = models.ForeignKey(TypeContributionSystem, related_name="%(app_label)s_%(class)s_type_pension")
    pension = models.ForeignKey(ContributionSystem, related_name="%(app_label)s_%(class)s_pension")
    number_pension = models.CharField(max_length=12, blank=True, verbose_name='CUSPP')
    salud = models.ForeignKey(ContributionSystem, related_name="%(app_label)s_%(class)s_salud")
    sctr = models.ForeignKey(ContributionSystem, related_name="%(app_label)s_%(class)s_sctr")
    is_affiliate_surefire = models.BooleanField(default=False)
    is_affiliate_syndicate = models.BooleanField(default=False)
    type_via = models.CharField(max_length=10, choices=core_constants.TYPE_TYPE_VIA_OPTIONS)
    name_via = models.CharField(max_length=150, blank=True)
    nro_via = models.CharField(max_length=10, blank=True, null=True)
    interior = models.CharField(max_length=10, blank=True, null=True)
    manzana = models.CharField(max_length=20, blank=True, null=True)
    type_zone = models.CharField(max_length=10, choices=core_constants.TYPE_TYPE_ZONE_OPTIONS)
    name_zone = models.CharField(max_length=100, blank=True, null=True)
    residence = models.CharField(max_length=255, blank=True)
    observations = models.TextField(null=True, blank=True)
    picture = models.FileField(null=True, blank=True, upload_to="foto/")
    dni = models.FileField(null=True, blank=True, upload_to="dni/")
    qualification = models.CharField(max_length=10, default='3',
                                     choices=core_constants.TYPE_QUALIFICATION_OPTIONS)
    email = models.EmailField(blank=True, null=True)
    specialty = models.ForeignKey(Specialty, related_name="%(app_label)s_%(class)s_specialty")
    bank = models.ForeignKey(Bank, related_name="%(app_label)s_%(class)s_bank")
    number_bank_account = models.CharField(max_length=20, blank=True, null=True)
    number_interbanking = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return "{0}{1}".format(self.first_name, self.last_name)


class BloodRelative(models.Model):
    employee = models.ForeignKey(Employee, related_name="%(app_label)s_%(class)s_employee")
    document_type = models.CharField(
        max_length=20, null=True, blank=True,
        choices=core_constants.SELECT_DEFAULT + core_constants.TYPE_IDENTITY_DOCUMENT_OPTIONS)
    document_number = models.CharField(max_length=20, null=True, blank=True)
    first_name = models.CharField(_('first name'), max_length=100, blank=True, null=True, unique=False)
    last_name = models.CharField(_('last name'), max_length=100, blank=True, null=True, unique=False)
    kinship = models.CharField(max_length=10, choices=core_constants.TYPE_KINSHIP_OPTIONS)
    birth_date = models.DateField()
    file_kinship = models.FileField(null=True, blank=True, upload_to="kinship/")

    def __str__(self):
        return self.employee.first_name


class ExperienceRecord(models.Model):
    employee = models.ForeignKey(Employee, related_name="%(app_label)s_%(class)s_employee")
    name_company = models.CharField(max_length=120)
    ruc_company = models.CharField(max_length=120)
    Specialty_cargo = models.ForeignKey(Specialty, related_name="%(app_label)s_%(class)s_specialty")
    initial = models.DateField()
    final = models.DateField()
    type_document = models.CharField(max_length=10, choices=core_constants.TYPE_EXP_RECORD_OPTIONS)
    file_type_document = models.FileField(null=True, blank=True, upload_to="exp_record/")
    total_mes = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.employee.first_name


class TrainingRecord(models.Model):
    employee = models.ForeignKey(Employee, related_name="%(app_label)s_%(class)s_employee")
    name_institution = models.CharField(max_length=120)
    course = models.TextField(max_length=100)
    initial = models.DateField()
    final = models.DateField()
    file_trainer = models.FileField(null=True, blank=True, upload_to="exp_trainer/")
    total_dias = models.IntegerField(default=0, blank=True, null=True, )

    def __str__(self):
        return self.employee.first_name


class PoliceRecord(models.Model):
    employee = models.ForeignKey(Employee, related_name="%(app_label)s_%(class)s_employee")
    date_emission = models.DateField()
    type_doc_police = models.CharField(max_length=10, choices=core_constants.TYPE_POLICE_RECORD_OPTIONS)
    result_type_doc_police = models.CharField(max_length=10, choices=core_constants.STATUS_FILE_RECORD_OPTIONS)
    observation = models.TextField(blank=True)
    file_police = models.FileField(null=True, blank=True, upload_to="police_record/")

    def __str__(self):
        return self.employee.first_name


class BloodRecord(models.Model):
    employee = models.ForeignKey(Employee, related_name="%(app_label)s_%(class)s_employee")
    type_doc_blood = models.CharField(max_length=10, choices=core_constants.TYPE_BLOOD_RECORD_OPTIONS)
    date_emission = models.DateField()
    result_type_doc_blood = models.CharField(max_length=10, choices=core_constants.STATUS_FILE_RECORD_OPTIONS)
    observation = models.TextField(max_length=200, null=True, blank=True)
    file_blood = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.employee.first_name


class Eps(models.Model):
    employee = models.ForeignKey(Employee, related_name="%(app_label)s_%(class)s_employee")
    eps = models.ForeignKey(ContributionSystem, related_name="%(app_label)s_%(class)s_eps")
    valor = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.employee.first_name

from django.db import models

from core.utils.fields import BaseModel


class Zone(BaseModel):
    name = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        unique_together = ["name"]

    def __str__(self):
        return self.name


class Country(BaseModel):
    zone = models.ForeignKey(Zone, related_name="%(app_label)s_%(class)s_zone")
    name = models.CharField(max_length=50, null=True, blank=True)
    code = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    iso_code = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        unique_together = ["zone", "name"]

    def __str__(self):
        return self.name


class State(BaseModel):
    zone = models.ForeignKey(Zone, related_name="%(app_label)s_%(class)s_zone")
    country = models.ForeignKey(
        Country, related_name="%(app_label)s_%(class)s_country")
    name = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        unique_together = ["zone", "country", "name"]

    def __str__(self):
        return self.name

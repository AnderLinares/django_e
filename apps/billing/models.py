from django.db import models

from core.utils.fields import BaseModel


class TypeDocument(BaseModel):
    name = models.CharField(max_length=200, null=True, blank=True)
    abbreviation = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        unique_together = ["name"]

    def __str__(self):
        return self.name


class TypePayment(BaseModel):
    name = models.CharField(max_length=200, null=True, blank=True)
    abbreviation = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        unique_together = ["name"]

    def __str__(self):
        return self.name

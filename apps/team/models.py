from django.db import models

from core.utils.fields import BaseModel2, BaseModel


class Module(BaseModel):
    name = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        unique_together = ["name"]

    def __str__(self):
        return self.name


class Team(BaseModel):
    name = models.CharField(max_length=100, null=True, blank=True)
    module = models.ManyToManyField(Module, related_name="%(app_label)s_%(class)s_module")

    def get_module_list(self):
        return "\n".join([p.name for p in self.module.all()])

    class Meta:
        unique_together = ["name"]

    def __str__(self):
        return self.name

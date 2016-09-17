from django.db import models

from core.models import Team, Module
from core.utils.fields import BaseModel, BaseModuleModel


class Menu(BaseModuleModel):
    """ model Menu(menu) """
    module = models.ForeignKey(
        Module, related_name="%(app_label)s_%(class)s_module")
    order = models.IntegerField(default=0, null=False, blank=False)

    class Meta:
        ordering = ['order']
        unique_together = ['name', 'module']

    @classmethod
    def children_menu(cls):
        return cls

    def __str__(self):
        return "{0}-{1}".format(str(self.module.name), str(self.name))


class MenuItem(BaseModuleModel):
    """ model MenuItem(menu item) """
    menu = models.ForeignKey(
        Menu, related_name="%(app_label)s_%(class)s_menu")
    reference = models.CharField(
        unique=True, max_length=100, null=False, blank=False)
    order = models.IntegerField(null=False, blank=False, default=0)

    def menu_text(self):
        return self.menu.name

    class Meta:
        ordering = ['menu']
        unique_together = ['reference']

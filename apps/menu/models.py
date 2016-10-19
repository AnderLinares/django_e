from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from core.utils.fields import BaseModuleModel, BaseModel
from apps.team.models import Team


class MenuPermissions(BaseModel):
    name = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        unique_together = ["name"]

    def __str__(self):
        return self.name


class Menu(BaseModuleModel):
    order = models.IntegerField(default=0, null=False, blank=False)

    class Meta:
        ordering = ['order']
        unique_together = ['name']

    def __str__(self):
        return "{0}".format(str(self.name))


class MenuItem(BaseModuleModel):
    menu = models.ForeignKey(Menu, related_name="%(app_label)s_%(class)s_menu")
    reference = models.CharField(
        unique=True, max_length=100, null=False, blank=False)
    order = models.IntegerField(null=False, blank=False, default=0)

    def menu_text(self):
        return self.menu.name

    class Meta:
        ordering = ['menu']

    def __str__(self):
        return "{0}-{1}".format(str(self.menu.name), str(self.reference))


class TeamMenu(BaseModel):
    team = models.ForeignKey(Team, related_name="%(app_label)s_%(class)s_team")
    menu = models.ForeignKey(Menu, related_name="%(app_label)s_%(class)s_menu")
    permissions_menu = models.ManyToManyField(
        MenuPermissions, related_name="%(app_label)s_%(class)s_permissions_menu")

    def get_permission_menu_list(self):
        return ",\n".join([p.name for p in self.permissions_menu.all()])

    class Meta:
        unique_together = ['team', 'menu']

    def __str__(self):
        return "{0}-{1}".format(self.team, self.menu)


class TeamMenuItem(BaseModel):
    team_menu = models.ForeignKey(
        TeamMenu, related_name="%(app_label)s_%(class)s_team_menu")
    menu_item = models.ForeignKey(
        MenuItem, related_name="%(app_label)s_%(class)s_menu_item")

    class Meta:
        unique_together = ['team_menu', 'menu_item']

    def __str__(self):
        return "{0}-{1}".format(self.team_menu, self.menu_item)

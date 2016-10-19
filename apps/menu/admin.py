from django.contrib import admin

from .models import (
    Menu, MenuItem,
    TeamMenu, TeamMenuItem)


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    ordering = ('order',)
    extra = 0


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ["name", 'order', 'match', 'is_deleted']
    fieldsets = [
        ["Menu", {
            "fields": ('name', 'order', 'style', 'match')
        }],

    ]
    inlines = [MenuItemInline, ]


class TeamMenuItemInline(admin.TabularInline):
    list_display = ['team_menu', 'menu_item']
    model = TeamMenuItem
    extra = 0

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        field = super().formfield_for_foreignkey(db_field, request, **kwargs)
        if db_field.name == "menu_item":
            if request._obj is not None:
                field.queryset = MenuItem.objects.filter(menu=request._obj.menu)
            else:
                field.queryset = field.queryset.none()
        return field


@admin.register(TeamMenu)
class TeamMenuAdmin(admin.ModelAdmin):
    list_display = ['team', 'menu']
    inlines = [TeamMenuItemInline, ]

    def get_form(self, request, obj=None, **kwargs):
        request._obj = obj
        return super().get_form(request, obj, **kwargs)

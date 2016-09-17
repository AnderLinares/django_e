from django.contrib import admin

from .models import (
    Menu, MenuItem)


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    ordering = ('order',)
    extra = 0


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ["module", "name", 'order', 'match', 'is_deleted']
    fieldsets = [
        ["Menu", {
            "fields": ("module", 'name', 'order', 'style', 'match')
        }],

    ]
    inlines = [MenuItemInline, ]


@admin.register(MenuItem)
class SubMenuAdmin(admin.ModelAdmin):
    list_display = ["name", 'order', 'menu_text', 'reference', 'is_deleted']
    fieldsets = [
        ["SubModule", {
            "fields": ('name', 'menu', 'order', 'style', 'match', 'reference')
        }],

    ]



# class GroupSubModuleInline(admin.TabularInline):
#     list_display = ['group_module', 'submodule']
#     model = GroupSubModule
#     extra = 0
#
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         field = super(GroupSubModuleInline, self).formfield_for_foreignkey(
#             db_field, request, **kwargs)
#         if db_field.name == 'submodule':
#             if request._obj_ is not None:
#                 field.queryset = field.queryset.filter(
#                     module=request._obj_.module)
#             else:
#                 field.queryset = field.queryset.none()
#         return field


# @admin.register(GroupMenu)
# class GroupModuleAdmin(admin.ModelAdmin):
#     list_display = ['group', 'module']
#     inlines = [GroupSubModuleInline, ]
#
#     def get_form(self, request, obj=None, **kwargs):
#         request._obj_ = obj
#         return super(GroupModuleAdmin, self).get_form(request, obj, **kwargs)

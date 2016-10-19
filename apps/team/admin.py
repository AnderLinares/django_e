# from django.contrib import admin
#
# from .models import (
#     Module, Team, TeamModule, TeamMenu, TeamSubMenu
# )

# admin.site.register(Module)
# admin.site.register(Team)

#
# class ModuleInline(admin.TabularInline):
#     model = Team.module.through
#
#
# @admin.register(Team)
# class TeamAdmin(admin.ModelAdmin):
#     inlines = [
#         ModuleInline,
#     ]
#     exclude = ('module',)
#
#
# class TeamSubMenuAdminInline(admin.TabularInline):
#     model = TeamSubMenu
#     list_display = ['group_menu', 'menu_item']
#     extra = 0
#
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         field = super().formfield_for_foreignkey(db_field, request, **kwargs)
#         if db_field.name == 'menu_item':
#             if request._obj is not None:
#                 field.queryset = field.queryset.filter(menu=request._obj.menu)
#             else:
#                 field.queryset = field.queryset.none()
#         return field
#
#
# @admin.register(TeamMenu)
# class TeamMenuAdmin(admin.ModelAdmin):
#     inlines = [TeamSubMenuAdminInline, ]
#
#     def get_form(self, request, obj=None, **kwargs):
#         request._obj = obj
#         return super().get_form(request, obj, **kwargs)

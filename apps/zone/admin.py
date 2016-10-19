from django.contrib import admin

from .models import Zone

admin.site.register(Zone)
# admin.site.register(Country)
# admin.site.register(State)


# class CountryAdminInline(admin.TabularInline):
#     model = Country
#
#
# @admin.register(Zone)
# class ZoneAdmin(admin.ModelAdmin):
#     inlines = [CountryAdminInline, ]
#
#
# class StateAdminInline(admin.TabularInline):
#     model = State
#
#
# @admin.register(Country)
# class CountryAdmin(admin.ModelAdmin):
#     inlines = [StateAdminInline]

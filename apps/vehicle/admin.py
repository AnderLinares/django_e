from django.contrib import admin

from .models import Vehicle, VehicleDetail, VehicleImage

admin.site.register(VehicleDetail)


class VehicleImageAdminInline(admin.TabularInline):
    model = VehicleImage


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    inlines = [VehicleImageAdminInline, ]

from django.contrib import admin

from .models import (
    Bank, ContributionSystem, Currency, ExchangeRate, Person, VehicleFuel,
    Service, Specialty, TypeContributionSystem, UnitMeasurement,
    VehicleBrand, VehicleModel, VehicleEnrollment, VehicleInventory, Store,
    ProductBrand, ProductModel
)

admin.site.register(Bank)
admin.site.register(ContributionSystem)
admin.site.register(Currency)
admin.site.register(ExchangeRate)
admin.site.register(Person)
admin.site.register(VehicleFuel)
admin.site.register(Service)
admin.site.register(Specialty)
admin.site.register(TypeContributionSystem)
admin.site.register(UnitMeasurement)
admin.site.register(VehicleBrand)
admin.site.register(VehicleModel)
admin.site.register(VehicleEnrollment)
admin.site.register(VehicleInventory)
admin.site.register(Store)
admin.site.register(ProductBrand)
admin.site.register(ProductModel)


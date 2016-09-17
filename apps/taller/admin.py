from django.contrib import admin

from .models import (
    Brand, Labour, TypeJob, TypeVehicle, Vehicle,
    Quotation, QuotationDetail, Order, OrderDetail, OrderDocument,
    OrderSupervision
)

admin.site.register(Brand)
admin.site.register(Labour)
admin.site.register(TypeJob)
admin.site.register(TypeVehicle)
admin.site.register(Vehicle)
admin.site.register(Quotation)
admin.site.register(QuotationDetail)

admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(OrderDocument)
admin.site.register(OrderSupervision)

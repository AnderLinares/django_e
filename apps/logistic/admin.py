from django.contrib import admin

from .models import PurchaseOrder, PurchaseOrderDetail

admin.site.register(PurchaseOrder)
admin.site.register(PurchaseOrderDetail)

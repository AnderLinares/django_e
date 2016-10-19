from django.contrib import admin

# Register your models here.
from .models import PurchaseOrderStore, PurchaseOrderStoreDetail

admin.site.register(PurchaseOrderStore)
admin.site.register(PurchaseOrderStoreDetail)
from django.contrib import admin

from .models import Supplier, SupplierProduct, SupplierSubsidiary


admin.site.register(Supplier)
admin.site.register(SupplierSubsidiary)
admin.site.register(SupplierProduct)
from django.contrib import admin

# Register your models here.
from .models import QuotationMaintenance, QuotationMaintenanceDetail

admin.site.register(QuotationMaintenance)
admin.site.register(QuotationMaintenanceDetail)
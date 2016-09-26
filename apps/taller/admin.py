from django.contrib import admin

from .models import (
    Brand, Labour, TypeLabour, TypeTransport, Vehicle,
    Quotation, QuotationDetail,
    ReportDocument, Report, TypeCheckList, LabourCheckList,
    TransportInventory, ServiceCheckList, SolicitudeCheckList,
    CheckList, CheckListDetail, InventoryCheckList, PhotoCheckList,
    LabourEmployeeCheckList

)

admin.site.register(Brand)
admin.site.register(Labour)
admin.site.register(TypeLabour)
admin.site.register(TypeTransport)

admin.site.register(Vehicle)
admin.site.register(Quotation)
admin.site.register(QuotationDetail)

admin.site.register(Report)
admin.site.register(ReportDocument)

admin.site.register(ServiceCheckList)
admin.site.register(TypeCheckList)
admin.site.register(TransportInventory)
admin.site.register(SolicitudeCheckList)
# admin.site.register(LabourCheckList)

# admin.site.register(SupervisionCheckList)


class CheckListDetailInline(admin.TabularInline):
    model = CheckListDetail
    extra = 1
    min_num = 1
    max_num = 2


class InventoryCheckListInline(admin.TabularInline):
    model = InventoryCheckList
    extra = 1
    min_num = 1
    max_num = 1


class PhotoCheckListInline(admin.TabularInline):
    model = PhotoCheckList
    extra = 1
    min_num = 1
    max_num = 4


class LabourCheckListInline(admin.TabularInline):
    model = LabourCheckList
    extra = 1
    min_num = 1
    max_num = 1


@admin.register(CheckList)
class CheckListAdmin(admin.ModelAdmin):
    inlines = [CheckListDetailInline]


@admin.register(CheckListDetail)
class CheckListDetailAdmin(admin.ModelAdmin):
    inlines = [InventoryCheckListInline, PhotoCheckListInline, LabourCheckListInline]


class LabourEmployeeCheckListInline(admin.TabularInline):
    model = LabourEmployeeCheckList
    extra = 1
    min_num = 1
    max_num = 5


@admin.register(LabourCheckList)
class CheckListAdmin(admin.ModelAdmin):
    inlines = [LabourEmployeeCheckListInline]
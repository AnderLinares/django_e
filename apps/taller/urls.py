from django.conf.urls import url, include

from .views import (
    BrandView, BrandCreateView, BrandEditView, BrandListView,
    LabourView, LabourCreateView, LabourEditView, LabourListView,
    TypeJobCreateView, TypeJobView, TypeJobEditView, TypeJobListView,
    VehicleView, VehicleCreateView, VehicleEditView, VehicleListView,
    QuotationView, QuotationCreateView, QuotationEditView, QuotationListView,
    ReportView, ReportCreateView, ReportEditView, ReportListView,
    OrderRentalView,
    TypeCheckListView, TypeCheckListCreateView, TypeCheckListEditView, TypeCheckListListView,
    TypeVehicleCreateView, TypeVehicleView, TypeVehicleEditView, TypeVehicleListView,
)

brand_patterns = ([
   url(r'^$', BrandView.as_view(), name="index"),
   url(r'^add/', BrandCreateView.as_view(), name="add"),
   url(r'^edit/', BrandEditView.as_view(), name="edit"),
   url(r'^list/', BrandListView.as_view(), name="list"),
], 'admin-brand')

type_job_patterns = ([
   url(r'^$', TypeJobView.as_view(), name="index"),
   url(r'^add/', TypeJobCreateView.as_view(), name="add"),
   url(r'^edit/', TypeJobEditView.as_view(), name="edit"),
   url(r'^list/', TypeJobListView.as_view(), name="list"),
], 'admin-typejob')

type_vehicle_patterns = ([
   url(r'^$', TypeVehicleView.as_view(), name="index"),
   url(r'^add/', TypeVehicleCreateView.as_view(), name="add"),
   url(r'^edit/', TypeVehicleEditView.as_view(), name="edit"),
   url(r'^list/', TypeVehicleListView.as_view(), name="list"),
], 'admin-typevehicle')

labour_patterns = ([
   url(r'^$', LabourView.as_view(), name="index"),
   url(r'^add/', LabourCreateView.as_view(), name="add"),
   url(r'^edit/', LabourEditView.as_view(), name="edit"),
   url(r'^list/', LabourListView.as_view(), name="list"),
], 'admin-labour')

vehicle_patterns = ([
   url(r'^$', VehicleView.as_view(), name="index"),
   url(r'^add/', VehicleCreateView.as_view(), name="add"),
   url(r'^edit/', VehicleEditView.as_view(), name="edit"),
   url(r'^list/', VehicleListView.as_view(), name="list"),
], 'admin-vehicle')

type_checklist_patterns = ([
   url(r'^$', TypeCheckListView.as_view(), name="index"),
   url(r'^add/', TypeCheckListCreateView.as_view(), name="add"),
   url(r'^edit/', TypeCheckListEditView.as_view(), name="edit"),
   url(r'^list/', TypeCheckListListView.as_view(), name="list"),
], 'admin-typechecklist')

quotation_patterns = ([
   url(r'^$', QuotationView.as_view(), name="index"),
   url(r'^add/', QuotationCreateView.as_view(), name="add"),
   url(r'^edit/', QuotationEditView.as_view(), name="edit"),
   url(r'^list/', QuotationListView.as_view(), name="list"),
], 'quotation-solicitude')


report_patterns = ([
   url(r'^$', ReportView.as_view(), name="index"),
   url(r'^add/', ReportCreateView.as_view(), name="add"),
   url(r'^edit/', ReportEditView.as_view(), name="edit"),
   url(r'^list/', ReportListView.as_view(), name="list"),
], 'report-solicitude')

order_alquiler_patterns = ([
   url(r'^$', OrderRentalView.as_view(), name="index"),
   url(r'^add/', ReportCreateView.as_view(), name="add"),
   url(r'^edit/', ReportEditView.as_view(), name="edit"),
   url(r'^list/', ReportListView.as_view(), name="list"),
], 'order-alquiler')


urlpatterns = [
    url(r'^brand/', include(brand_patterns)),
    url(r'^labour/', include(labour_patterns)),
    url(r'^typejob/', include(type_job_patterns)),
    url(r'^typevehicle/', include(type_vehicle_patterns)),
    url(r'^typechecklist/', include(type_checklist_patterns)),
    url(r'^vehicle/', include(vehicle_patterns)),
    url(r'^quotation/', include(quotation_patterns)),
    url(r'^report/', include(report_patterns)),
    url(r'^order-alquiler/', include(order_alquiler_patterns)),
]


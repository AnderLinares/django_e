from django.conf.urls import url, include

from .views import (
    BrandView, BrandCreateView, BrandEditView, BrandListView,
    LabourView, LabourCreateView, LabourEditView, LabourListView,
    TypeLabourCreateView, TypeLabourView, TypeLabourEditView, TypeLabourListView,
    VehicleView, VehicleCreateView, VehicleEditView, VehicleListView,
    QuotationView, QuotationCreateView, QuotationEditView, QuotationListView,
    ReportView, ReportCreateView, ReportEditView, ReportListView,
    # OrderRentalView,
    TypeCheckListView, TypeCheckListCreateView, TypeCheckListEditView, TypeCheckListListView,
    TypeTransportCreateView, TypeTransportView, TypeTransportEditView, TypeTransportListView,
    ChecklistCreateView, ChecklistMaintenanceView,
    LabourEmployeeView, LabourEmployeeListView, LabourEmployeeTaskView)

brand_patterns = ([
   url(r'^$', BrandView.as_view(), name="index"),
   url(r'^add/', BrandCreateView.as_view(), name="add"),
   url(r'^edit/', BrandEditView.as_view(), name="edit"),
   url(r'^list/', BrandListView.as_view(), name="list"),
], 'admin-brand')

type_job_patterns = ([
   url(r'^$', TypeLabourView.as_view(), name="index"),
   url(r'^add/', TypeLabourCreateView.as_view(), name="add"),
   url(r'^edit/', TypeLabourEditView.as_view(), name="edit"),
   url(r'^list/', TypeLabourListView.as_view(), name="list"),
], 'admin-typejob')

type_vehicle_patterns = ([
   url(r'^$', TypeTransportView.as_view(), name="index"),
   url(r'^add/', TypeTransportCreateView.as_view(), name="add"),
   url(r'^edit/', TypeTransportEditView.as_view(), name="edit"),
   url(r'^list/', TypeTransportListView.as_view(), name="list"),
], 'admin-typetransport')

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

checklist_patterns = ([
   url(r'^$', ChecklistCreateView.as_view(), name="index"),
   url(r'^list-maintenance/', ChecklistMaintenanceView.as_view(), name="maintenance-solicitude"),
   url(r'^list-labour/', LabourEmployeeView.as_view(), name="list-labour"),
   # url(r'^list/', ReportListView.as_view(), name="list"),
], 'checklist')

checklist_labour_patterns = ([
   url(r'^$', LabourEmployeeView.as_view(), name="index"),
   url(r'^list/', LabourEmployeeListView.as_view(), name="list"),
   url(r'^add-task/', LabourEmployeeTaskView.as_view(), name="add-task"),
], 'checklist-labour')


urlpatterns = [
    url(r'^brand/', include(brand_patterns)),
    url(r'^labour/', include(labour_patterns)),
    url(r'^typelabour/', include(type_job_patterns)),
    url(r'^typetransport/', include(type_vehicle_patterns)),
    url(r'^typechecklist/', include(type_checklist_patterns)),
    url(r'^vehicle/', include(vehicle_patterns)),
    url(r'^quotation/', include(quotation_patterns)),
    url(r'^report/', include(report_patterns)),
    url(r'^checklist/', include(checklist_patterns)),
    url(r'^checklist-labour/', include(checklist_labour_patterns)),
]


from json import loads

from django.contrib import messages
from django.db import transaction
from django.views.generic import ListView
from django.views.generic import TemplateView

from core import constants as core_constants
from core.mixins import TemplateLoginRequiredMixin
from core.models import Correlative
from core.utils.funct_formset import CoreFormset
from .constants import *
from .forms import (
    BrandForm, LabourForm, TypeLabourForm, VehicleForm, QuotationForm,
    ReportForm, TypeCheckListForm,
    CheckListForm,
    TypeTransportForm, CheckListDetailForm)
from .formset import (
    ReportDocumentFormSet, CheckListPhotoFormSet,
    CheckListInventoryFormSet, CheckListLabourFormSet, CheckListLabourEmployeeFormSet)
from .models import (
    Brand, Labour, Vehicle, Quotation, QuotationDetail,
    Report, TypeCheckList, TypeLabour, TypeTransport, ServiceCheckList, CheckListDetail,
    LabourCheckList, LabourEmployeeCheckList)

# Brand
class BrandView(TemplateLoginRequiredMixin, ListView):
    model = Brand
    template_name = 'pages/taller/brand/brand.html'
    context_object_name = "brand_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Brand List"
        return context


class BrandListView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/taller/brand/brand_list.html'

    def get(self, request, *args, **kwargs):
        self.brand = Brand.objects.all()
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brand_list'] = self.brand
        return context


class BrandCreateView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/taller/brand/brand_form.html'

    def get(self, request, *args, **kwargs):
        self.form_brand = BrandForm(auto_id='id_brand_%s')
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        data = loads(request.body.decode('utf-8'))
        data_form_brand = data['form']
        self.form_brand = BrandForm(data=data_form_brand, auto_id='id_brand_%s')
        if self.form_brand.is_valid():
            self.form_brand.save()
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_brand"] = self.form_brand
        return context


class BrandEditView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/taller/brand/brand_form.html'

    def get(self, request, *args, **kwargs):
        brand = request.GET['brand_id']
        self.brand = Brand.objects.get(service=brand)
        self.form_brand = BrandForm(
            auto_id='id_brand_%s', instance=self.brand)
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        data = loads(request.body.decode('utf-8'))
        data_brand_pk = data['form_pk']
        data_form_brand = data['form']
        self.brand = Brand.objects.get(service=data_brand_pk)
        self.form_brand = BrandForm(
            data_form_brand, auto_id='id_brand_%s', instance=self.brand)

        if self.form_brand.is_valid():
            self.form_brand.save()
            messages.success(request, core_constants.STATUS_MSG_TAGS['success'])
        else:
            messages.error(request, core_constants.STATUS_MSG_TAGS['error'])
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_brand'] = self.form_brand
        context['form_pk'] = self.brand.id
        context['btn_edit'] = core_constants.CODE_TEXT_EDIT
        return context


# Labour
class LabourView(TemplateLoginRequiredMixin, ListView):
    model = Labour
    template_name = 'pages/taller/labour/labour.html'
    context_object_name = "labour_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Labour List"
        return context


class LabourListView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/taller/labour/labour_list.html'

    def get(self, request, *args, **kwargs):
        self.labour = Labour.objects.all()
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['labour_list'] = self.labour
        return context


class LabourCreateView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/taller/labour/labour_form.html'

    def get(self, request, *args, **kwargs):
        self.form_labour = LabourForm(auto_id='id_labour_%s')
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        data = loads(request.body.decode('utf-8'))
        data_form_labour = data['form']
        self.form_labour = LabourForm(data=data_form_labour, auto_id='id_labour_%s')
        if self.form_labour.is_valid():
            self.form_labour.save()
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_labour"] = self.form_labour
        return context


class LabourEditView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/taller/labour/labour_form.html'

    def get(self, request, *args, **kwargs):
        labour = request.GET['labour_id']
        self.labour = Labour.objects.get(service=labour)
        self.form_labour = LabourForm(
            auto_id='id_labour_%s', instance=self.labour)
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        data = loads(request.body.decode('utf-8'))
        data_labour_pk = data['form_pk']
        data_form_labour = data['form']
        self.labour = Labour.objects.get(service=data_labour_pk)
        self.form_labour = LabourForm(
            data_form_labour, auto_id='id_labour_%s', instance=self.labour)

        if self.form_labour.is_valid():
            self.form_labour.save()
            messages.success(request, core_constants.STATUS_MSG_TAGS['success'])
        else:
            messages.error(request, core_constants.STATUS_MSG_TAGS['error'])
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_labour'] = self.form_labour
        context['form_pk'] = self.labour.id
        context['btn_edit'] = core_constants.CODE_TEXT_EDIT
        return context


# Typejob
class TypeLabourView(TemplateLoginRequiredMixin, ListView):
    model = TypeLabour
    template_name = 'pages/taller/typetransport/typetransport.html'
    context_object_name = "typejob_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Typejob List"
        return context


class TypeLabourListView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/taller/typetransport/typetransport_list.html'

    def get(self, request, *args, **kwargs):
        self.typejob = TypeLabour.objects.all()
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['typejob_list'] = self.typejob
        return context


class TypeLabourCreateView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/taller/typetransport/typetransport_form.html'

    def get(self, request, *args, **kwargs):
        self.form_typejob = TypeLabourForm(auto_id='id_typejob_%s')
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        data = loads(request.body.decode('utf-8'))
        data_form_typejob = data['form']
        self.form_typejob = TypeLabourForm(data=data_form_typejob, auto_id='id_typejob_%s')
        if self.form_typejob.is_valid():
            self.form_typejob.save()
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_typejob"] = self.form_typejob
        return context


class TypeLabourEditView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/taller/typetransport/typetransport_form.html'

    def get(self, request, *args, **kwargs):
        typejob = request.GET['typejob_id']
        self.typejob = TypeLabour.objects.get(service=typejob)
        self.form_typejob = TypeLabourForm(
            auto_id='id_typejob_%s', instance=self.typejob)
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        data = loads(request.body.decode('utf-8'))
        data_typejob_pk = data['form_pk']
        data_form_typejob = data['form']
        self.typejob = TypeLabour.objects.get(service=data_typejob_pk)
        self.form_typejob = TypeLabourForm(
            data_form_typejob, auto_id='id_typejob_%s', instance=self.typejob)

        if self.form_typejob.is_valid():
            self.form_typejob.save()
            messages.success(request, core_constants.STATUS_MSG_TAGS['success'])
        else:
            messages.error(request, core_constants.STATUS_MSG_TAGS['error'])
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_typejob'] = self.form_typejob
        context['form_pk'] = self.typejob.id
        context['btn_edit'] = core_constants.CODE_TEXT_EDIT
        return context


# Typevehicle
class TypeTransportView(TemplateLoginRequiredMixin, ListView):
    model = TypeTransport
    template_name = 'pages/taller/typetransport/typetransport.html'
    context_object_name = "typetransport_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Type Vehicle List"
        return context


class TypeTransportListView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/taller/typetransport/typetransport_list.html'

    def get(self, request, *args, **kwargs):
        self.typetransport = TypeTransport.objects.all()
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['typetransport_list'] = self.typetransport
        return context


class TypeTransportCreateView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/taller/typetransport/typetransport_form.html'

    def get(self, request, *args, **kwargs):
        self.form_typetransport = TypeTransportForm(auto_id='id_typetransport_%s')
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        data = loads(request.body.decode('utf-8'))
        data_form_typetransport = data['form']
        self.form_typetransport = TypeTransportForm(data=data_form_typetransport, auto_id='id_typetransport_%s')
        if self.form_typetransport.is_valid():
            self.form_typetransport.save()
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_typetransport"] = self.form_typetransport
        return context


class TypeTransportEditView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/taller/typetransport/typetransport_form.html'

    def get(self, request, *args, **kwargs):
        typetransport = request.GET['typetransport_id']
        self.typetransport = TypeTransport.objects.get(service=typetransport)
        self.form_typetransport = TypeTransportForm(
            auto_id='id_typetransport_%s', instance=self.typetransport)
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        data = loads(request.body.decode('utf-8'))
        data_typetransport_pk = data['form_pk']
        data_form_typetransport = data['form']
        self.typetransport = TypeTransport.objects.get(service=data_typetransport_pk)
        self.form_typetransport = TypeLabourForm(
            data_form_typetransport, auto_id='id_typetransport_%s', instance=self.typetransport)

        if self.form_typetransport.is_valid():
            self.form_typetransport.save()
            messages.success(request, core_constants.STATUS_MSG_TAGS['success'])
        else:
            messages.error(request, core_constants.STATUS_MSG_TAGS['error'])
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_typetransport'] = self.form_typetransport
        context['form_pk'] = self.typetransport.id
        context['btn_edit'] = core_constants.CODE_TEXT_EDIT
        return context


# TypeCheckList
class TypeCheckListView(TemplateLoginRequiredMixin, ListView):
    model = TypeCheckList
    template_name = 'pages/taller/typechecklist/typechecklist.html'
    context_object_name = "typechecklist_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Typechecklist List"
        return context


class TypeCheckListListView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/taller/typechecklist/typechecklist_list.html'

    def get(self, request, *args, **kwargs):
        self.typechecklist = TypeCheckList.objects.all()
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['typechecklist_list'] = self.typechecklist
        return context


class TypeCheckListCreateView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/taller/typechecklist/typechecklist_form.html'

    def get(self, request, *args, **kwargs):
        self.form_typechecklist = TypeCheckListForm(auto_id='id_typechecklist_%s')
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        data = loads(request.body.decode('utf-8'))
        data_form_typechecklist = data['form']
        self.form_typechecklist = TypeCheckListForm(
            data=data_form_typechecklist, auto_id='id_typechecklist_%s')
        if self.form_typechecklist.is_valid():
            self.form_typechecklist.save()
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_typechecklist"] = self.form_typechecklist
        return context


class TypeCheckListEditView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/taller/typechecklist/typechecklist_form.html'

    def get(self, request, *args, **kwargs):
        typechecklist = request.GET['typechecklist_id']
        self.typechecklist = TypeCheckList.objects.get(service=typechecklist)
        self.form_typechecklist = TypeCheckListForm(
            auto_id='id_typechecklist_%s', instance=self.typechecklist)
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        data = loads(request.body.decode('utf-8'))
        data_typechecklist_pk = data['form_pk']
        data_form_typechecklist = data['form']
        self.typechecklist = TypeCheckList.objects.get(service=data_typechecklist_pk)
        self.form_typechecklist = TypeCheckListForm(
            data_form_typechecklist, auto_id='id_typechecklist_%s', instance=self.typechecklist)

        if self.form_typechecklist.is_valid():
            self.form_typechecklist.save()
            messages.success(request, core_constants.STATUS_MSG_TAGS['success'])
        else:
            messages.error(request, core_constants.STATUS_MSG_TAGS['error'])
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_typechecklist'] = self.form_typechecklist
        context['form_pk'] = self.typechecklist.id
        context['btn_edit'] = core_constants.CODE_TEXT_EDIT
        return context


# Vehicle
class VehicleView(TemplateLoginRequiredMixin, ListView):
    model = Vehicle
    template_name = 'pages/taller/vehicle/vehicle.html'
    context_object_name = "vehicle_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Vehicle List"
        return context


class VehicleListView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/taller/vehicle/vehicle_list.html'

    def get(self, request, *args, **kwargs):
        self.vehicle = Vehicle.objects.all()
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vehicle_list'] = self.vehicle
        return context


class VehicleCreateView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/taller/vehicle/vehicle_form.html'

    def get(self, request, *args, **kwargs):
        self.form_vehicle = VehicleForm(auto_id='id_vehicle_%s')
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        data = loads(request.body.decode('utf-8'))
        data_form_vehicle = data['form']
        self.form_vehicle = VehicleForm(data=data_form_vehicle, auto_id='id_vehicle_%s')
        if self.form_vehicle.is_valid():
            self.form_vehicle.save(user=self.request.user, commit=False)
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_vehicle"] = self.form_vehicle
        return context


class VehicleEditView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/taller/vehicle/vehicle_form.html'

    def get(self, request, *args, **kwargs):
        vehicle = request.GET['vehicle_id']
        self.vehicle = Vehicle.objects.get(pk=vehicle)
        self.form_vehicle = VehicleForm(
            auto_id='id_vehicle_%s', instance=self.vehicle)
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        data = loads(request.body.decode('utf-8'))
        data_vehicle_pk = data['form_pk']
        data_form_vehicle = data['form']
        self.vehicle = Vehicle.objects.get(pk=data_vehicle_pk)
        self.form_vehicle = VehicleForm(
            data_form_vehicle, auto_id='id_vehicle_%s', instance=self.vehicle)
        if self.form_vehicle.is_valid():
            self.form_vehicle.save(user=self.request.user, commit=False)
            messages.success(request, core_constants.STATUS_MSG_TAGS['success'])
        else:
            messages.error(request, core_constants.STATUS_MSG_TAGS['error'])
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_vehicle'] = self.form_vehicle
        context['form_pk'] = self.vehicle.id
        context['btn_edit'] = core_constants.CODE_TEXT_EDIT
        return context


# Quotation
class QuotationView(TemplateLoginRequiredMixin, ListView):
    model = Quotation
    template_name = 'pages/taller/quotation/quotation.html'
    context_object_name = "quotation_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Quotation List"
        return context


class QuotationListView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/taller/quotation/quotation_list.html'

    def get(self, request, *args, **kwargs):
        self.quotation = Quotation.objects.all()
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quotation_list'] = self.quotation
        return context


class QuotationCreateView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/taller/quotation/quotation_form.html'

    def get(self, request, *args, **kwargs):
        self.form_quotation = QuotationForm(auto_id='id_quotation_%s')
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        data = loads(request.body.decode('utf-8'))
        data_form_quo = data["form_quo"]
        data_form_quotation = data["form"]
        data_form_detail = data["form_quo_detail"]
        self.form_quotation = QuotationForm(data=data_form_quotation, auto_id='id_quotation_%s')
        if self.form_quotation.is_valid():
            self.form_quotation.save(data_form_quo, data_form_detail, commit=False)
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_quotation"] = self.form_quotation
        return context


class QuotationEditView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/taller/quotation/quotation_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.form_quotation_detail = None
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        quotation = request.GET['quotation_id']
        self.form_quotation = Quotation.objects.get(pk=quotation)
        self.form_quotation_detail = QuotationDetail.objects.filter(quotation=quotation)
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_quotation'] = self.form_quotation
        context['form_quotation_detail'] = self.form_quotation_detail
        context['btn_edit'] = core_constants.CODE_TEXT_EDIT
        return context


# Report
class ReportView(TemplateLoginRequiredMixin, ListView):
    model = Report
    template_name = 'pages/taller/report/report.html'
    context_object_name = "report_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Report List"
        return context


class ReportListView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/taller/report/report_list.html'

    def get(self, request, *args, **kwargs):
        self.report = Report.objects.all()
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['report_list'] = self.report
        return context


class ReportCreateView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/taller/report/report_form.html'

    def __init__(self, **kwargs):
        self.rptdoc_prefix = 'report_doc'
        super().__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        self.form_report = ReportForm(auto_id='id_report_%s')
        self.form_report_document = ReportDocumentFormSet(
            prefix=self.rptdoc_prefix)
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        data = loads(request.body.decode('utf-8'))
        data_form_report = data['form']
        self.form_report = ReportForm(data=data_form_report, auto_id='id_report_%s')
        self.form_report_document = ReportDocumentFormSet(
            data_form_report, prefix=self.rptdoc_prefix)
        if self.form_report.is_valid() and self.form_report_document.is_valid():
            form_report = self.form_report.save(user=self.request.user, commit=False)
            self.get_formset_rpt_doc(self.form_report_document, form_report)
        return super().render_to_response(self.get_context_data())

    @staticmethod
    def get_formset_rpt_doc(formset, report):
        for form in formset.forms:
            form.save(report=report, commit=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_report"] = self.form_report
        context["form_report_doc"] = self.form_report_document
        return context


class ReportEditView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/taller/report/report_form.html'

    def __init__(self, **kwargs):
        self.rptdoc_prefix = 'report_doc'
        super().__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        report = request.GET['report_id']
        self.report = Report.objects.get(service=report)
        self.form_report = ReportForm(
            auto_id='id_report_%s', instance=self.report)
        self.form_report_document = ReportDocumentFormSet(
            prefix=self.rptdoc_prefix, instance=self.report)
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        data = loads(request.body.decode('utf-8'))
        data_report_pk = data['form_pk']
        data_form_report = data['form']
        self.report = Report.objects.get(service=data_report_pk)
        self.form_report = ReportForm(
            data_form_report, auto_id='id_report_%s', instance=self.report)
        self.form_report_document = ReportDocumentFormSet(
            data_form_report, prefix=self.rptdoc_prefix, instance=self.report)
        if self.form_report.is_valid() and self.form_report_document.is_valid():
            form_report = self.form_report.save(user=self.request.user, commit=False)
            self.get_formset_rpt_doc(self.form_report_document, form_report)
            messages.success(request, core_constants.STATUS_MSG_TAGS['success'])
        else:
            messages.error(request, core_constants.STATUS_MSG_TAGS['error'])
        return super().render_to_response(self.get_context_data())

    @staticmethod
    def get_formset_rpt_doc(formset, report):
        for form in formset.forms:
            form.save(report=report, commit=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_report_doc"] = self.form_report_document
        context['form_report'] = self.form_report
        context['form_pk'] = self.report.id
        context['btn_edit'] = core_constants.CODE_TEXT_EDIT
        return context


# checklist
class ChecklistCreateView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/taller/checklist/checklist.html'

    def __init__(self, **kwargs):

        self.id_checklist = 'id_checklist_%s'
        self.id_checklist_detail = 'id_checklist_detail_%s'
        self.checklist_inventory_prefix = 'checklist_inventory'
        # self.id_checklist_inventory = 'id_checklist_inventory_%s'
        self.checklist_photo_prefix = 'checklist_photo'
        self.checklist_labour_prefix = 'checklist_labour'
        # self.id_checklist_labour = 'id_checklist_labour_%s'
        super().__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        current_correlative = Correlative.get_current_correlative_checklist(
            subsidiary=self.request.user.get_subsidiary(), type_correlative=core_constants.CODE_CORRELATIVE_CHECKLIST)
        initial_checklist = {'number_billing': current_correlative["exact_number"]}
        self.form_checklist = CheckListForm(initial=initial_checklist, auto_id=self.id_checklist)
        self.form_checklist_detail = CheckListDetailForm(auto_id=self.id_checklist_detail)
        self.form_checklist_inventory = CheckListInventoryFormSet(prefix=self.checklist_inventory_prefix)
        self.form_checklist_photo = CheckListPhotoFormSet(prefix=self.checklist_photo_prefix)
        self.form_checklist_labour = CheckListLabourFormSet(prefix=self.checklist_labour_prefix)
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        print(request.POST)
        self.form_checklist = CheckListForm(
            request.POST, auto_id=self.id_checklist)
        self.form_checklist_detail = CheckListDetailForm(
            request.POST, auto_id=self.id_checklist_detail)
        self.form_checklist_inventory = CheckListInventoryFormSet(
            request.POST, prefix=self.checklist_inventory_prefix)
        self.form_checklist_photo = CheckListPhotoFormSet(
            request.POST, request.FILES, prefix=self.checklist_photo_prefix)
        self.form_checklist_labour = CheckListLabourFormSet(
            request.POST, prefix=self.checklist_labour_prefix)

        if (self.form_checklist.is_valid() and
                self.form_checklist_detail.is_valid() and
                self.form_checklist_inventory.is_valid() and
                self.form_checklist_photo.is_valid() and
                self.form_checklist_labour.is_valid()):
            with transaction.atomic():
                user = self.request.user
                checklist = self.form_checklist.save(user=user, commit=False)
                checklist_detail = self.form_checklist_detail.save(checklist=checklist, commit=False)
                # self.form_checklist_inventory.save(checklist_detail=checklist_detail, commit=False)
                CoreFormset.formset_checklist_inventory(self.form_checklist_inventory, checklist_detail)
                CoreFormset.formset_checklist_photo(self.form_checklist_photo, checklist_detail)
                CoreFormset.formset_checklist_labour(self.form_checklist_labour, checklist_detail)
                # self.form_checklist_labour.save(checklist_detail=checklist_detail, commit=False)

                current_correlative = Correlative.get_current_correlative_checklist(
                    subsidiary=user.get_subsidiary(),
                    type_correlative=core_constants.CODE_CORRELATIVE_CHECKLIST)
                Correlative.get_correlative_update(
                    subsidiary=user.get_subsidiary(),
                    type_correlative=core_constants.CODE_CORRELATIVE_CHECKLIST,
                    actual_number=current_correlative["actual_correlative"])
                current_correlative = Correlative.get_current_correlative_checklist(
                    subsidiary=user.get_subsidiary(), type_correlative=core_constants.CODE_CORRELATIVE_CHECKLIST)
                initial_checklist = {'number_billing': current_correlative["exact_number"]}
                self.form_checklist = CheckListForm(initial=initial_checklist, auto_id=self.id_checklist)
                self.form_checklist_detail = CheckListDetailForm(auto_id=self.id_checklist_detail)
                self.form_checklist_inventory = CheckListInventoryFormSet(prefix=self.checklist_inventory_prefix)
                self.form_checklist_photo = CheckListPhotoFormSet(prefix=self.checklist_photo_prefix)
                self.form_checklist_labour = CheckListLabourFormSet(prefix=self.checklist_labour_prefix)
            messages.success(request, core_constants.STATUS_MSG_TAGS['success'])
        else:
            messages.error(request, core_constants.STATUS_MSG_TAGS['error'])
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_checklist"] = self.form_checklist
        context["form_checklist_detail"] = self.form_checklist_detail
        context["formset_checklist_inventory"] = self.form_checklist_inventory
        context["formset_checklist_photo"] = self.form_checklist_photo
        context["formset_checklist_labour"] = self.form_checklist_labour
        return context


# checklist-Maintenance
class ChecklistMaintenanceView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/taller/checklist/checklist_maintenance.html'

    def get(self, request, *args, **kwargs):
        maintenance = ServiceCheckList.objects.all()
        self.checklist_detail_maintenance = CheckListDetail.objects.filter(service_checklist=maintenance)
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_checklist_maintenance"] = self.checklist_detail_maintenance
        return context


# checklistlabour Employee
class LabourEmployeeView(TemplateLoginRequiredMixin, ListView):
    model = LabourCheckList
    template_name = 'pages/taller/checklist_labour/checklist_labour.html'
    context_object_name = "labour_employees"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Labour Employee List"
        return context


class LabourEmployeeListView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/taller/checklist_labour/checklist_labour_list.html'

    def get(self, request, *args, **kwargs):
        self.labour_employees = LabourCheckList.objects.all()
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['labour_employees'] = self.labour_employees
        return context


class LabourEmployeeTaskView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/taller/checklist_labour/checklist_labour_task_form.html'

    def __init__(self, **kwargs):
        self.labour_employee_prefix = 'labour_employee'
        super().__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        checklist_labour_id = request.GET['checklist_labour_id']
        self.labour_checklist = LabourCheckList.objects.get(pk=checklist_labour_id)
        self.formset_labour_employee = CheckListLabourEmployeeFormSet(
            prefix=self.labour_employee_prefix, instance=self.labour_checklist)
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        data = loads(request.body.decode('utf-8'))
        print(data)
        data_labour_employee_pk = data['form_pk']
        data_form_labour_employee = data['form']
        self.labour_checklist = LabourCheckList.objects.get(pk=data_labour_employee_pk)
        self.formset_labour_employee = CheckListLabourEmployeeFormSet(
            data_form_labour_employee, prefix=self.labour_employee_prefix)
        if self.formset_labour_employee.is_valid():
            CoreFormset.formset_checklist_labour_employee(
                self.formset_labour_employee, self.labour_checklist)
            messages.success(request, core_constants.STATUS_MSG_TAGS['success'])
        else:
            messages.error(request, core_constants.STATUS_MSG_TAGS['error'])
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formset_labour_employee'] = self.formset_labour_employee
        context['form_pk'] = self.labour_checklist.id
        context['btn_edit'] = core_constants.CODE_TEXT_EDIT
        return context
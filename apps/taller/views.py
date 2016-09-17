from json import loads

from django.contrib import messages
from django.views.generic import ListView
from django.views.generic import TemplateView

from core import constants as core_constants
from core.mixins import TemplateLoginRequiredMixin
from .forms import (
    BrandForm, LabourForm, TypeJobForm, VehicleForm, QuotationForm)
from .models import Brand, Labour, TypeJob, Vehicle, Quotation


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
        self.brand = Brand.objects.get(pk=brand)
        self.form_brand = BrandForm(
            auto_id='id_brand_%s', instance=self.brand)
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        data = loads(request.body.decode('utf-8'))
        data_brand_pk = data['form_pk']
        data_form_brand = data['form']
        self.brand = Brand.objects.get(pk=data_brand_pk)
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
        self.labour = Labour.objects.get(pk=labour)
        self.form_labour = LabourForm(
            auto_id='id_labour_%s', instance=self.labour)
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        data = loads(request.body.decode('utf-8'))
        data_labour_pk = data['form_pk']
        data_form_labour = data['form']
        self.labour = Labour.objects.get(pk=data_labour_pk)
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
class TypeJobView(TemplateLoginRequiredMixin, ListView):
    model = TypeJob
    template_name = 'pages/taller/typejob/typejob.html'
    context_object_name = "typejob_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Typejob List"
        return context


class TypeJobListView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/taller/typejob/typejob_list.html'

    def get(self, request, *args, **kwargs):
        self.typejob = TypeJob.objects.all()
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['typejob_list'] = self.typejob
        return context


class TypeJobCreateView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/taller/typejob/typejob_form.html'

    def get(self, request, *args, **kwargs):
        self.form_typejob = TypeJobForm(auto_id='id_typejob_%s')
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        data = loads(request.body.decode('utf-8'))
        data_form_typejob = data['form']
        self.form_typejob = TypeJobForm(data=data_form_typejob, auto_id='id_typejob_%s')
        if self.form_typejob.is_valid():
            self.form_typejob.save()
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_typejob"] = self.form_typejob
        return context


class TypeJobEditView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/taller/typejob/typejob_form.html'

    def get(self, request, *args, **kwargs):
        typejob = request.GET['typejob_id']
        self.typejob = TypeJob.objects.get(pk=typejob)
        self.form_typejob = TypeJobForm(
            auto_id='id_typejob_%s', instance=self.typejob)
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        data = loads(request.body.decode('utf-8'))
        data_typejob_pk = data['form_pk']
        data_form_typejob = data['form']
        self.typejob = TypeJob.objects.get(pk=data_typejob_pk)
        self.form_typejob = TypeJobForm(
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
        data_form_quotation = data['form']
        self.form_quotation = QuotationForm(data=data_form_quotation, auto_id='id_quotation_%s')
        if self.form_quotation.is_valid():
            self.form_quotation.save(commit=False)
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_quotation"] = self.form_quotation
        return context


class QuotationEditView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/taller/quotation/quotation_form.html'

    def get(self, request, *args, **kwargs):
        quotation = request.GET['quotation_id']
        self.quotation = Quotation.objects.get(pk=quotation)
        self.form_quotation = QuotationForm(
            auto_id='id_quotation_%s', instance=self.quotation)
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        data = loads(request.body.decode('utf-8'))
        data_quotation_pk = data['form_pk']
        data_form_quotation = data['form']
        self.quotation = Quotation.objects.get(pk=data_quotation_pk)
        self.form_quotation = QuotationFormForm(
            data_form_quotation, auto_id='id_quotation_%s', instance=self.quotation)
        if self.form_quotation.is_valid():
            self.form_quotation.save(commit=False)
            messages.success(request, core_constants.STATUS_MSG_TAGS['success'])
        else:
            messages.error(request, core_constants.STATUS_MSG_TAGS['error'])
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_quotation'] = self.form_quotation
        context['form_pk'] = self.quotation.id
        context['btn_edit'] = core_constants.CODE_TEXT_EDIT
        return context

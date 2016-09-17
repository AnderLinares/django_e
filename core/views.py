from json import loads

from django.contrib import messages
from django.views.generic import ListView
from django.views.generic import TemplateView

from core import constants as core_constants
from core.mixins import TemplateLoginRequiredMixin
from .forms import (
    CurrencyForm, ExchangeRateForm, OrganizationForm, SubsidiaryForm, UnitMeasurementForm
)
from .models import Currency, ExchangeRate, Organization, Subsidiary, UnitMeasurement


# currency
class CurrencyView(TemplateLoginRequiredMixin, ListView):
    model = Currency
    template_name = 'pages/core/currency/currency.html'
    context_object_name = "currency_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Currency List"
        return context


class CurrencyListView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/core/currency/currency_list.html'

    def get(self, request, *args, **kwargs):
        self.currency = Currency.objects.all()
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['currency_list'] = self.currency
        return context


class CurrencyCreateView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/core/currency/currency_form.html'

    def get(self, request, *args, **kwargs):
        self.form_currency = CurrencyForm(auto_id='id_currency_%s')
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        data = loads(request.body.decode('utf-8'))
        data_form_currency = data['form']
        self.form_currency = CurrencyForm(data=data_form_currency, auto_id='id_currency_%s')
        if self.form_currency.is_valid():
            self.form_currency.save()
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_currency"] = self.form_currency
        return context


class CurrencyEditView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/core/currency/currency_form.html'

    def get(self, request, *args, **kwargs):
        currency = request.GET['currency_id']
        self.currency = Currency.objects.get(pk=currency)
        self.form_currency = CurrencyForm(
            auto_id='id_currency_%s', instance=self.currency)
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        data = loads(request.body.decode('utf-8'))
        data_currency_pk = data['form_pk']
        data_form_currency = data['form']
        self.currency = Currency.objects.get(pk=data_currency_pk)
        self.form_currency = CurrencyForm(
            data_form_currency, auto_id='id_currency_%s', instance=self.currency)
        if self.form_currency.is_valid():
            self.form_currency.save()
            messages.success(request, core_constants.STATUS_MSG_TAGS['success'])
        else:
            messages.error(request, core_constants.STATUS_MSG_TAGS['error'])
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_currency'] = self.form_currency
        context['form_pk'] = self.currency.id
        context['btn_edit'] = core_constants.CODE_TEXT_EDIT
        return context


# Exchange rate
class ExchangeRateView(TemplateLoginRequiredMixin, ListView):
    model = ExchangeRate
    template_name = 'pages/core/exchangerate/exchangerate.html'
    context_object_name = "exchangerate_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Exchange Rate List"
        return context


class ExchangeRateListView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/core/exchangerate/exchangerate_list.html'

    def get(self, request, *args, **kwargs):
        self.exchange_rate = ExchangeRate.objects.all()
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exchangerate_list'] = self.exchange_rate
        return context


class ExchangeRateCreateView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/core/exchangerate/exchangerate_form.html'

    def get(self, request, *args, **kwargs):
        self.form_exchange_rate = ExchangeRateForm(auto_id='id_exchange_rate_%s')
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        data = loads(request.body.decode('utf-8'))
        data_form_exchange_rate = data['form']
        self.form_exchange_rate = ExchangeRateForm(data=data_form_exchange_rate, auto_id='id_exchange_rate_%s')
        if self.form_exchange_rate.is_valid():
            self.form_exchange_rate.save()
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_exchangerate"] = self.form_exchange_rate
        return context


class ExchangeRateEditView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/core/exchangerate/exchangerate_form.html'

    def get(self, request, *args, **kwargs):
        exchange_rate = request.GET['exchangerate_id']
        self.exchange_rate = ExchangeRate.objects.get(pk=exchange_rate)
        self.form_exchange_rate = ExchangeRateForm(
            auto_id='id_exchange_rate_%s', instance=self.exchange_rate)
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        data = loads(request.body.decode('utf-8'))
        data_exchange_rate_pk = data['form_pk']
        data_form_exchange_rate = data['form']
        self.exchange_rate = ExchangeRate.objects.get(pk=data_exchange_rate_pk)
        self.form_exchange_rate = ExchangeRateForm(
            data_form_exchange_rate, auto_id='id_exchange_rate_%s', instance=self.exchange_rate)
        if self.form_exchange_rate.is_valid():
            self.form_exchange_rate.save()
            messages.success(request, core_constants.STATUS_MSG_TAGS['success'])
        else:
            messages.error(request, core_constants.STATUS_MSG_TAGS['error'])
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_exchangerate'] = self.form_exchange_rate
        context['form_pk'] = self.exchange_rate.id
        context['btn_edit'] = core_constants.CODE_TEXT_EDIT
        return context


# Organization
class OrganizationView(TemplateLoginRequiredMixin, ListView):
    model = Organization
    template_name = 'pages/core/organization/organization.html'
    context_object_name = "organization_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Organization List"
        return context


class OrganizationListView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/core/organization/organization_list.html'

    def get(self, request, *args, **kwargs):
        self.organization = Organization.objects.all()
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['organization_list'] = self.organization
        return context


class OrganizationCreateView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/core/organization/organization_form.html'

    def get(self, request, *args, **kwargs):
        self.form_organization = OrganizationForm(auto_id='id_organization_%s')
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        data = loads(request.body.decode('utf-8'))
        data_form_organization = data['form']
        self.form_organization = OrganizationForm(data=data_form_organization, auto_id='id_organization_%s')
        if self.form_organization.is_valid():
            self.form_organization.save()
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_organization"] = self.form_organization
        return context


class OrganizationEditView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/core/organization/organization_form.html'

    def get(self, request, *args, **kwargs):
        organization = request.GET['organization_id']
        self.organization = Organization.objects.get(pk=organization)
        self.form_organization = OrganizationForm(
            auto_id='id_organization_%s', instance=self.organization)
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        data = loads(request.body.decode('utf-8'))
        data_organization_pk = data['form_pk']
        data_form_organization = data['form']
        self.organization = Organization.objects.get(pk=data_organization_pk)
        self.form_organization = OrganizationForm(
            data_form_organization, auto_id='id_organization_%s', instance=self.organization)
        if self.form_organization.is_valid():
            self.form_organization.save()
            messages.success(request, core_constants.STATUS_MSG_TAGS['success'])
        else:
            messages.error(request, core_constants.STATUS_MSG_TAGS['error'])
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_organization'] = self.form_organization
        context['form_pk'] = self.organization.id
        context['btn_edit'] = core_constants.CODE_TEXT_EDIT
        return context


# Subsidiary
class SubsidiaryView(TemplateLoginRequiredMixin, ListView):
    model = Subsidiary
    template_name = 'pages/core/subsidiary/subsidiary.html'
    context_object_name = "subsidiary_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Subsidiary List"
        return context


class SubsidiaryListView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/core/subsidiary/subsidiary_list.html'

    def get(self, request, *args, **kwargs):
        self.subsidiary = Subsidiary.objects.all()
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subsidiary_list'] = self.subsidiary
        return context


class SubsidiaryCreateView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/core/subsidiary/subsidiary_form.html'

    def get(self, request, *args, **kwargs):
        self.form_subsidiary = SubsidiaryForm(auto_id='id_subsidiary_%s')
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        data = loads(request.body.decode('utf-8'))
        data_form_subsidiary = data['form']
        self.form_subsidiary = SubsidiaryForm(data=data_form_subsidiary, auto_id='id_subsidiary_%s')
        if self.form_subsidiary.is_valid():
            self.form_subsidiary.save()
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_subsidiary"] = self.form_subsidiary
        return context


class SubsidiaryEditView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/core/subsidiary/subsidiary_form.html'

    def get(self, request, *args, **kwargs):
        subsidiary = request.GET['subsidiary_id']
        self.subsidiary = Subsidiary.objects.get(pk=subsidiary)
        self.form_subsidiary = SubsidiaryForm(
            auto_id='id_subsidiary_%s', instance=self.subsidiary)
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        data = loads(request.body.decode('utf-8'))
        data_subsidiary_pk = data['form_pk']
        data_form_subsidiary = data['form']
        self.subsidiary = Subsidiary.objects.get(pk=data_subsidiary_pk)
        self.form_subsidiary = SubsidiaryForm(
            data_form_subsidiary, auto_id='id_subsidiary_%s', instance=self.subsidiary)
        if self.form_subsidiary.is_valid():
            self.form_subsidiary.save()
            messages.success(request, core_constants.STATUS_MSG_TAGS['success'])
        else:
            messages.error(request, core_constants.STATUS_MSG_TAGS['error'])
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_subsidiary'] = self.form_subsidiary
        context['form_pk'] = self.subsidiary.id
        context['btn_edit'] = core_constants.CODE_TEXT_EDIT
        return context


# UnitMeasurement
class UnitMeasurementView(TemplateLoginRequiredMixin, ListView):
    model = UnitMeasurement
    template_name = 'pages/core/unit_measurement/unit_measurement.html'
    context_object_name = "measurement_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Measurement List"
        return context


class UnitMeasurementListView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/core/unit_measurement/unit_measurement_list.html'

    def get(self, request, *args, **kwargs):
        self.unit_measurement = UnitMeasurement.objects.all()
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['measurement_list'] = self.unit_measurement
        return context


class UnitMeasurementCreateView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/core/unit_measurement/unit_measurement_form.html'

    def get(self, request, *args, **kwargs):
        self.form_measurement = UnitMeasurementForm(auto_id='id_measurement_%s')
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        data = loads(request.body.decode('utf-8'))
        data_form_measurement = data['form']
        self.form_measurement = UnitMeasurementForm(data=data_form_measurement, auto_id='id_measurement_%s')
        if self.form_measurement.is_valid():
            self.form_measurement.save()
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_measurement"] = self.form_measurement
        return context


class UnitMeasurementEditView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/core/unit_measurement/unit_measurement_form.html'

    def get(self, request, *args, **kwargs):
        unit_measurement = request.GET['measurement_id']
        self.unit_measurement = UnitMeasurement.objects.get(pk=unit_measurement)
        self.form_measurement = UnitMeasurementForm(
            auto_id='id_measurement_%s', instance=self.unit_measurement)
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        data = loads(request.body.decode('utf-8'))
        data_measurement_pk = data['form_pk']
        data_form_measurement = data['form']
        self.unit_measurement = UnitMeasurement.objects.get(pk=data_measurement_pk)
        self.form_measurement = UnitMeasurementForm(
            data_form_measurement, auto_id='id_measurement_%s', instance=self.unit_measurement)
        if self.form_measurement.is_valid():
            self.form_measurement.save()
            messages.success(request, core_constants.STATUS_MSG_TAGS['success'])
        else:
            messages.error(request, core_constants.STATUS_MSG_TAGS['error'])
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_measurement'] = self.form_measurement
        context['form_pk'] = self.unit_measurement.id
        context['btn_edit'] = core_constants.CODE_TEXT_EDIT
        return context
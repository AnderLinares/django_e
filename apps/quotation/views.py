from json import loads

from django.db import transaction
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from apps.company.models import Correlative
from core.mixins import AuthListView, AuthDeleteView, AuthTemplateCreateView, AuthDetailView
from core.models import TaxConfiguration
from .forms import QuotationStoreForm, QuotationMaintenanceForm
from .models import QuotationStore, QuotationStoreDetail, QuotationMaintenance, QuotationMaintenanceDetail


class QuotationStoreList(AuthListView):
    template_name = 'dashboard/pages/quotation/qt_store/qt_store_list.html'
    model = QuotationStore
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("list QuotationStore")
        return context


class QuotationStoreCreation(AuthTemplateCreateView):
    template_name = 'dashboard/pages/quotation/qt_store/qt_store_form.html'

    def get(self, request, *args, **kwargs):
        _subsidiary = self.request.user.get_profile
        code_qt = Correlative.get_current_document('COP', _subsidiary.subsidiary)
        parameter = dict(code_qt=code_qt, user=_subsidiary.user)
        self.form = QuotationStoreForm(initial=parameter)
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        data = loads(request.body.decode('utf-8'))
        data_form = data["form"]
        data_form_detail = data["form_detail"]
        form = QuotationStoreForm(data=data_form)
        if form.is_valid():
            return self.frm_valid(form, data_form_detail)
        else:
            return self.frm_invalid(form)

    def frm_valid(self, form, form_detail):
        with transaction.atomic():
            qt_store = form.save(commit=True)
            for qt_detail in form_detail:
                q_detail = QuotationStoreDetail()
                q_detail.quotation_store = qt_store
                q_detail.product_id = qt_detail["product"]
                q_detail.quantity = qt_detail["quantity"]
                q_detail.save()
            _subsidiary = self.request.user.get_profile
            Correlative.save_current_document('COP', _subsidiary.subsidiary)
            self.form = form
        return super().render_to_response(self.get_context_data())

    def frm_invalid(self, form):
        self.form = form
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form
        return context


class QuotationStoreDetailView(AuthDetailView):
    template_name = 'dashboard/pages/quotation/qt_store/qt_store_detail.html'
    model = QuotationStore

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qt_list"] = QuotationStoreDetail.objects.filter(quotation_store_id=self.kwargs["pk"])
        return context


class QuotationStoreDelete(AuthDeleteView):
    template_name = 'dashboard/pages/quotation/qt_store/qt_store_confirm_delete.html'
    model = QuotationStore
    success_url = reverse_lazy('QuotationStore:list')


"""
    QuotationMaintenance
"""


class QuotationMaintenanceList(AuthListView):
    template_name = 'dashboard/pages/quotation/qt_maintenance/qt_maintenance_list.html'
    model = QuotationMaintenance
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("list QuotationMaintenance")
        return context


class QuotationMaintenanceCreation(AuthTemplateCreateView):
    template_name = 'dashboard/pages/quotation/qt_maintenance/qt_maintenance_form.html'

    def get(self, request, *args, **kwargs):
        _subsidiary = self.request.user.get_profile
        code_qt = Correlative.get_current_document('COM', _subsidiary.subsidiary)
        _igv = TaxConfiguration.get_igv_value()
        parameter = dict(code_qt=code_qt, user=_subsidiary.user, igv_tax=_igv)
        self.form = QuotationMaintenanceForm(initial=parameter)
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        data = loads(request.body.decode('utf-8'))
        data_form = data["form"]
        data_form_detail = data["form_detail"]
        form = QuotationMaintenanceForm(data=data_form)
        if form.is_valid():
            return self.frm_valid(form, data_form_detail)
        else:
            return self.frm_invalid(form)

    def frm_valid(self, form, form_detail):
        with transaction.atomic():
            qt_maintenance = form.save(commit=True)
            for qt_detail in form_detail:
                q_detail = QuotationMaintenanceDetail()
                q_detail.quotation_maintenance = qt_maintenance
                q_detail.description = qt_detail["description"]
                q_detail.quantity = qt_detail["quantity"]
                q_detail.unit_price = qt_detail["price"]
                q_detail.amount_price = qt_detail["importe"]
                q_detail.save()
            _subsidiary = self.request.user.get_profile
            Correlative.save_current_document('COM', _subsidiary.subsidiary)
            self.form = form
        return super().render_to_response(self.get_context_data())

    def frm_invalid(self, form):
        self.form = form
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form
        return context


class QuotationMaintenanceDetailView(AuthDetailView):
    template_name = 'dashboard/pages/quotation/qt_maintenance/qt_maintenance_detail.html'
    model = QuotationMaintenance

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qt_list"] = QuotationMaintenanceDetail.objects.filter(quotation_maintenance_id=self.kwargs["pk"])
        return context


class QuotationMaintenanceDelete(AuthDeleteView):
    template_name = 'dashboard/pages/quotation/qt_maintenance/qt_maintenance_confirm_delete.html'
    model = QuotationMaintenance
    success_url = reverse_lazy('QuotationMaintenance:list')

from json import loads

from django.conf import settings
from django.db import transaction
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView

from apps.company.models import Correlative
from core.mixins import AuthListView, AuthDeleteView, AuthTemplateCreateView, AuthDetailView
from .forms import QuotationStoreForm
from .models import QuotationStore, QuotationStoreDetail


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
        code_qt = Correlative.get_current_document('CO', _subsidiary.subsidiary)
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
        qt_store = form.save(commit=True)
        for qt_detail in form_detail:
            q_detail = QuotationStoreDetail()
            q_detail.quotation_store = qt_store
            q_detail.product_id = qt_detail["product"]
            q_detail.quantity = qt_detail["quantity"]
            q_detail.save()
        _subsidiary = self.request.user.get_profile
        Correlative.save_current_document('CO', _subsidiary.subsidiary)
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

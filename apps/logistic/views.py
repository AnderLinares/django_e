from json import loads

from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from apps.company.models import Correlative
from core.mixins import AuthListView, AuthDeleteView, AuthDetailView, \
    AuthTemplateCreateView
from core.models import TaxConfiguration
from .forms import (
    PurchaseOrderForm,
    PurchaseOrderDetailForm)
from .models import (
    PurchaseOrder, PurchaseOrderDetail
)

"""
    PurchaseOrder
"""


class PurchaseOrderList(AuthListView):
    template_name = 'dashboard/pages/logistic/po_store/po_store_list.html'
    model = PurchaseOrder
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("list Purchase Order")
        return context


class PurchaseOrderCreation(AuthTemplateCreateView):
    template_name = 'dashboard/pages/logistic/po_store/po_store_form.html'

    def get(self, request, *args, **kwargs):
        _subsidiary = self.request.user.get_profile
        code_po = Correlative.get_current_document('PO', _subsidiary.subsidiary)
        _igv = TaxConfiguration.get_igv_value()
        parameter = dict(code_po=code_po, user=_subsidiary.user, igv_tax=_igv)
        self.form = PurchaseOrderForm(initial=parameter)
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        data = loads(request.body.decode('utf-8'))
        data_form = data["form"]
        data_form_detail = data["form_detail"]
        form = PurchaseOrderForm(data=data_form)
        if form.is_valid():
            return self.frm_valid(form, data_form_detail)
        else:
            return self.frm_invalid(form)

    def frm_valid(self, form, form_detail):
        qt_store = form.save(commit=True)
        for po_detail in form_detail:
            p_detail = PurchaseOrderDetail()
            p_detail.purchase_order = qt_store
            p_detail.product_id = po_detail["product"]
            p_detail.description = po_detail["description"]
            p_detail.quantity = po_detail["quantity"]
            p_detail.unit_price = po_detail["price"]
            p_detail.discount = po_detail["discount"]
            p_detail.amount_price = po_detail["importe"]
            p_detail.save()
        _subsidiary = self.request.user.get_profile
        Correlative.save_current_document('PO', _subsidiary.subsidiary)
        self.form = form
        return super().render_to_response(self.get_context_data())

    def frm_invalid(self, form):
        self.form = form
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form
        return context


class PurchaseOrderDetailView(AuthDetailView):
    template_name = 'dashboard/pages/logistic/po_store/po_store_detail.html'
    model = PurchaseOrder

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["po_list"] = PurchaseOrderDetail.objects.filter(purchase_order_id=self.kwargs["pk"])
        return context


class PurchaseOrderDelete(AuthDeleteView):
    template_name = 'dashboard/pages/logistic/po_store/po_store_confirm_delete.html'
    model = PurchaseOrder
    success_url = reverse_lazy('PurchaseOrder:list')

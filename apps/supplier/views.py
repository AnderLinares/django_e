# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from core.mixins import AuthListView, AuthUpdateView, AuthCreateView, AuthDeleteView
from .forms import SupplierForm, SupplierSubsidiaryForm, SupplierProductForm
from .models import Supplier, SupplierSubsidiary, SupplierProduct

"""
    Supplier
"""


class SupplierList(AuthListView):
    template_name = 'dashboard/pages/supplier/supplier/supplier_list.html'
    model = Supplier
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("list Supplier")
        return context


class SupplierCreation(AuthCreateView):
    template_name = 'dashboard/pages/supplier/supplier/supplier_form.html'
    model = Supplier
    success_url = reverse_lazy('Supplier:list')
    form_class = SupplierForm


class SupplierUpdate(AuthUpdateView):
    template_name = 'dashboard/pages/supplier/supplier/supplier_form.html'
    model = Supplier
    success_url = reverse_lazy('Supplier:list')
    form_class = SupplierForm


class SupplierDelete(AuthDeleteView):
    template_name = 'dashboard/pages/supplier/supplier/supplier_confirm_delete.html'
    model = Supplier
    success_url = reverse_lazy('Supplier:list')


"""
    SupplierSubsidiary
"""


class SupplierSubsidiaryList(AuthListView):
    template_name = 'dashboard/pages/supplier/suppliersubsidiary/suppliersubsidiary_list.html'
    model = SupplierSubsidiary
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("list SupplierSubsidiary")
        return context


class SupplierSubsidiaryCreation(AuthCreateView):
    template_name = 'dashboard/pages/supplier/suppliersubsidiary/suppliersubsidiary_form.html'
    model = SupplierSubsidiary
    success_url = reverse_lazy('SupplierSubsidiary:list')
    form_class = SupplierSubsidiaryForm


class SupplierSubsidiaryUpdate(AuthUpdateView):
    template_name = 'dashboard/pages/supplier/suppliersubsidiary/suppliersubsidiary_form.html'
    model = SupplierSubsidiary
    success_url = reverse_lazy('SupplierSubsidiary:list')
    form_class = SupplierSubsidiaryForm


class SupplierSubsidiaryDelete(AuthDeleteView):
    template_name = 'dashboard/pages/supplier/suppliersubsidiary/suppliersubsidiary_confirm_delete.html'
    model = SupplierSubsidiary
    success_url = reverse_lazy('SupplierSubsidiary:list')


"""
    SupplierProduct
"""


class SupplierProductList(AuthListView):
    template_name = 'dashboard/pages/supplier/supplierproduct/supplierproduct_list.html'
    model = SupplierProduct
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("list SupplierProduct")
        return context


class SupplierProductCreation(AuthCreateView):
    template_name = 'dashboard/pages/supplier/supplierproduct/supplierproduct_form.html'
    model = SupplierProduct
    success_url = reverse_lazy('SupplierProduct:list')
    form_class = SupplierProductForm


class SupplierProductUpdate(AuthUpdateView):
    template_name = 'dashboard/pages/supplier/supplierproduct/supplierproduct_form.html'
    model = SupplierProduct
    success_url = reverse_lazy('SupplierProduct:list')
    form_class = SupplierProductForm


class SupplierProductDelete(AuthDeleteView):
    template_name = 'dashboard/pages/supplier/supplierproduct/supplierproduct_confirm_delete.html'
    model = SupplierProduct
    success_url = reverse_lazy('SupplierProduct:list')

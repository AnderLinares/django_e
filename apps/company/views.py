from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from .forms import OrganizationForm, SubsidiaryForm, CorrelativeForm
from .models import Correlative, Subsidiary, Organization
from core.mixins import AuthListView, AuthDeleteView, AuthUpdateView, AuthCreateView

"""
    Organization
"""


class OrganizationList(AuthListView):
    template_name = 'dashboard/pages/company/organization/organization_list.html'
    model = Organization
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("list Organization")
        return context


class OrganizationCreation(AuthCreateView):
    template_name = 'dashboard/pages/company/organization/organization_form.html'
    model = Organization
    success_url = reverse_lazy('Organization:list')
    form_class = OrganizationForm


class OrganizationUpdate(AuthUpdateView):
    template_name = 'dashboard/pages/company/organization/organization_form.html'
    model = Organization
    success_url = reverse_lazy('Organization:list')
    form_class = OrganizationForm


class OrganizationDelete(AuthDeleteView):
    template_name = 'dashboard/pages/company/organization/organization_confirm_delete.html'
    model = Organization
    success_url = reverse_lazy('Organization:list')


"""
    Subsidiary
"""


class SubsidiaryList(AuthListView):
    template_name = 'dashboard/pages/company/subsidiary/subsidiary_list.html'
    model = Subsidiary
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("list Subsidiary")
        return context


class SubsidiaryCreation(AuthCreateView):
    template_name = 'dashboard/pages/company/subsidiary/subsidiary_form.html'
    model = Subsidiary
    success_url = reverse_lazy('Subsidiary:list')
    form_class = SubsidiaryForm


class SubsidiaryUpdate(AuthUpdateView):
    template_name = 'dashboard/pages/company/subsidiary/subsidiary_form.html'
    model = Subsidiary
    success_url = reverse_lazy('Subsidiary:list')
    form_class = SubsidiaryForm


class SubsidiaryDelete(AuthDeleteView):
    template_name = 'dashboard/pages/company/subsidiary/subsidiary_confirm_delete.html'
    model = Subsidiary
    success_url = reverse_lazy('Subsidiary:list')

"""
    Correlative
"""


class CorrelativeList(AuthListView):
    template_name = 'dashboard/pages/company/correlative/correlative_list.html'
    model = Correlative
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("list Correlative")
        return context


class CorrelativeCreation(AuthCreateView):
    template_name = 'dashboard/pages/company/correlative/correlative_form.html'
    model = Correlative
    success_url = reverse_lazy('Correlative:list')
    form_class = CorrelativeForm


class CorrelativeUpdate(AuthUpdateView):
    template_name = 'dashboard/pages/company/correlative/correlative_form.html'
    model = Correlative
    success_url = reverse_lazy('Correlative:list')
    form_class = CorrelativeForm


class CorrelativeDelete(AuthDeleteView):
    template_name = 'dashboard/pages/company/correlative/correlative_confirm_delete.html'
    model = Correlative
    success_url = reverse_lazy('Correlative:list')
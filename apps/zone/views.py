# Create your views here.
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from core.mixins import AuthListView, AuthCreateView, AuthUpdateView, AuthDeleteView
from .forms import ZoneForm, CountryForm, StateForm
from .models import Zone, Country, State

"""
    Zone
"""


class ZoneList(AuthListView):
    template_name = 'dashboard/pages/zone/zone/zone_list.html'
    model = Zone
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("list Zone")
        return context


class ZoneCreation(AuthCreateView):
    template_name = 'dashboard/pages/zone/zone/zone_form.html'
    model = Zone
    success_url = reverse_lazy('Zone:list')
    form_class = ZoneForm


class ZoneUpdate(AuthUpdateView):
    template_name = 'dashboard/pages/zone/zone/zone_form.html'
    model = Zone
    success_url = reverse_lazy('Zone:list')
    form_class = ZoneForm


class ZoneDelete(AuthDeleteView):
    template_name = 'dashboard/pages/zone/zone/zone_confirm_delete.html'
    model = Zone
    success_url = reverse_lazy('Zone:list')


"""
    Country
"""


class CountryList(AuthListView):
    template_name = 'dashboard/pages/zone/country/country_list.html'
    model = Country
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("list Country")
        return context


class CountryCreation(AuthCreateView):
    template_name = 'dashboard/pages/zone/country/country_form.html'
    model = Country
    success_url = reverse_lazy('Country:list')
    form_class = CountryForm


class CountryUpdate(AuthUpdateView):
    template_name = 'dashboard/pages/zone/country/country_form.html'
    model = Country
    success_url = reverse_lazy('Country:list')
    form_class = CountryForm


class CountryDelete(AuthDeleteView):
    template_name = 'dashboard/pages/zone/zone/zone_confirm_delete.html'
    model = Country
    success_url = reverse_lazy('Country:list')


"""
    State
"""


class StateList(AuthListView):
    template_name = 'dashboard/pages/zone/state/state_list.html'
    model = State
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("list State")
        return context


class StateCreation(AuthCreateView):
    template_name = 'dashboard/pages/zone/state/state_form.html'
    model = State
    success_url = reverse_lazy('State:list')
    form_class = StateForm


class StateUpdate(AuthUpdateView):
    template_name = 'dashboard/pages/zone/state/state_form.html'
    model = State
    success_url = reverse_lazy('State:list')
    form_class = StateForm


class StateDelete(AuthDeleteView):
    template_name = 'dashboard/pages/zone/state/state_confirm_delete.html'
    model = State
    success_url = reverse_lazy('State:list')

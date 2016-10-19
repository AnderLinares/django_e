# Create your views here.
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from core.mixins import AuthListView, AuthUpdateView, AuthCreateView, AuthDeleteView
from .forms import ModuleForm, TeamForm
from .models import Module, Team

"""
    Module
"""


class ModuleList(AuthListView):
    template_name = 'dashboard/pages/team/module/module_list.html'
    model = Module
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("list Module")
        return context


class ModuleCreation(AuthCreateView):
    template_name = 'dashboard/pages/team/module/module_form.html'
    model = Module
    success_url = reverse_lazy('Module:list')
    form_class = ModuleForm


class ModuleUpdate(AuthUpdateView):
    template_name = 'dashboard/pages/team/module/module_form.html'
    model = Module
    success_url = reverse_lazy('Module:list')
    form_class = ModuleForm


class ModuleDelete(AuthDeleteView):
    template_name = 'dashboard/pages/team/module/module_confirm_delete.html'
    model = Module
    success_url = reverse_lazy('Module:list')


"""
    Team
"""


class TeamList(AuthListView):
    template_name = 'dashboard/pages/team/team/team_list.html'
    model = Team
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("list Team")
        return context


class TeamCreation(AuthCreateView):
    template_name = 'dashboard/pages/team/team/team_form.html'
    model = Team
    success_url = reverse_lazy('Team:list')
    form_class = TeamForm


class TeamUpdate(AuthUpdateView):
    template_name = 'dashboard/pages/team/team/team_form.html'
    model = Team
    success_url = reverse_lazy('Team:list')
    form_class = TeamForm


class TeamDelete(AuthDeleteView):
    template_name = 'dashboard/pages/team/team/team_confirm_delete.html'
    model = Team
    success_url = reverse_lazy('Team:list')





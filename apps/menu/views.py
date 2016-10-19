# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from core.mixins import AuthListView, AuthUpdateView, AuthCreateView, AuthDeleteView
from .forms import MenuForm, MenuItemForm, MenuPermissionsForm, TeamMenuItemForm, TeamMenuForm
from .models import Menu, MenuItem, MenuPermissions, TeamMenu, TeamMenuItem
from .formsets import TeamMenuItemFormSet

"""
    MenuPermissions
"""


class MenuPermissionsList(AuthListView):
    template_name = 'dashboard/pages/menu/menupermissions/menupermissions_list.html'
    model = MenuPermissions
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("list MenuPermissions")
        return context


class MenuPermissionsCreation(AuthCreateView):
    template_name = 'dashboard/pages/menu/menupermissions/menupermissions_form.html'
    model = MenuPermissions
    success_url = reverse_lazy('MenuPermissions:list')
    form_class = MenuPermissionsForm


class MenuPermissionsUpdate(AuthUpdateView):
    template_name = 'dashboard/pages/menu/menupermissions/menupermissions_form.html'
    model = MenuPermissions
    success_url = reverse_lazy('MenuPermissions:list')
    form_class = MenuPermissionsForm


class MenuPermissionsDelete(AuthDeleteView):
    template_name = 'dashboard/pages/menu/menupermissions/menupermissions_confirm_delete.html'
    model = MenuPermissions
    success_url = reverse_lazy('MenuPermissions:list')


"""
    Menu
"""


class MenuList(AuthListView):
    template_name = 'dashboard/pages/menu/menu/menu_list.html'
    model = Menu
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("list Menu")
        return context


class MenuCreation(AuthCreateView):
    template_name = 'dashboard/pages/menu/menu/menu_form.html'
    model = Menu
    success_url = reverse_lazy('Menu:list')
    form_class = MenuForm


class MenuUpdate(AuthUpdateView):
    template_name = 'dashboard/pages/menu/menu/menu_form.html'
    model = Menu
    success_url = reverse_lazy('Menu:list')
    form_class = MenuForm


class MenuDelete(AuthDeleteView):
    template_name = 'dashboard/pages/menu/menu/menu_confirm_delete.html'
    model = Menu
    success_url = reverse_lazy('Menu:list')


"""
    MenuItem
"""


class MenuItemList(AuthListView):
    template_name = 'dashboard/pages/menu/menuitem/menuitem_list.html'
    model = MenuItem
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("list MenuItem")
        return context


class MenuItemCreation(AuthCreateView):
    template_name = 'dashboard/pages/menu/menuitem/menuitem_form.html'
    model = MenuItem
    success_url = reverse_lazy('MenuItem:list')
    form_class = MenuItemForm


class MenuItemUpdate(AuthUpdateView):
    template_name = 'dashboard/pages/menu/menuitem/menuitem_form.html'
    model = MenuItem
    success_url = reverse_lazy('MenuItem:list')
    form_class = MenuItemForm


class MenuItemDelete(AuthDeleteView):
    template_name = 'dashboard/pages/menu/menuitem/menuitem_confirm_delete.html'
    model = MenuItem
    success_url = reverse_lazy('MenuItem:list')


"""
    TeamMenu
"""


class TeamMenuList(AuthListView):
    template_name = 'dashboard/pages/menu/teammenu/teammenu_list.html'
    model = TeamMenu
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("list TeamMenu")
        return context


class TeamMenuCreation(AuthCreateView):
    template_name = 'dashboard/pages/menu/teammenu/teammenu_form.html'
    model = TeamMenu
    success_url = reverse_lazy('TeamMenu:list')
    form_class = TeamMenuForm

    def __init__(self, **kwargs):
        self.prefix_team_menu_item = "t_menu_item_prefix"
        super().__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)
        self.team_menu_item_formset = TeamMenuItemFormSet(prefix=self.prefix_team_menu_item)
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        team_menu_item_formset = TeamMenuItemFormSet(
            self.request.POST, prefix=self.prefix_team_menu_item)
        if form.is_valid() and team_menu_item_formset.is_valid():
            return self.form_valid(form, team_menu_item_formset)
        else:
            return self.form_invalid(form, team_menu_item_formset)

    def form_valid(self, form, team_menu_item_formset):
        self.object = form.save()
        team_menu_item_formset.instance = self.object
        team_menu_item_formset.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, team_menu_item_formset):
        self.form = form
        self.team_menu_item_formset = team_menu_item_formset
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form
        context["team_menu_item_formset"] = self.team_menu_item_formset
        return context


class TeamMenuUpdate(AuthUpdateView):
    template_name = 'dashboard/pages/menu/teammenu/teammenu_form.html'
    model = TeamMenu
    success_url = reverse_lazy('TeamMenu:list')
    form_class = TeamMenuForm

    def __init__(self, **kwargs):
        self.prefix_team_menu_item = "t_menu_item_prefix"
        super().__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)
        self.team_menu_item_formset = TeamMenuItemFormSet(
            instance=self.object, prefix=self.prefix_team_menu_item)
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        team_menu_item_formset = TeamMenuItemFormSet(
            self.request.POST, instance=self.object, prefix=self.prefix_team_menu_item)
        if form.is_valid() and team_menu_item_formset.is_valid():
            return self.form_valid(form, team_menu_item_formset)
        else:
            return self.form_invalid(form, team_menu_item_formset)

    def form_valid(self, form, team_menu_item_formset):
        self.object = form.save()
        team_menu_item_formset.instance = self.object
        team_menu_item_formset.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, team_menu_item_formset):
        self.form = form
        self.team_menu_item_formset = team_menu_item_formset
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form
        context["team_menu_item_formset"] = self.team_menu_item_formset
        return context


class TeamMenuDelete(AuthDeleteView):
    template_name = 'dashboard/pages/menu/teammenu/teammenu_confirm_delete.html'
    model = TeamMenu
    success_url = reverse_lazy('TeamMenu:list')

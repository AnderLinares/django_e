from django import forms

from apps.team.models import Team
from .models import Menu, MenuItem, MenuPermissions, TeamMenu, TeamMenuItem


class MenuForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'Name', 'required': True,
             'class': 'form-control'})
        self.fields['order'].widget.attrs.update(
            {'placeholder': 'Order', 'required': True,
             'class': 'form-control'})
        self.fields['style'].widget.attrs.update(
            {'placeholder': 'Style', 'class': 'form-control'})
        self.fields['match'].widget.attrs.update(
            {'placeholder': 'Match', 'required': True,
             'class': 'form-control'})

    class Meta:
        model = Menu
        fields = "__all__"


class MenuItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['menu'].widget.attrs.update(
            {'placeholder': 'menu', 'required': True,
             'class': 'form-control'})
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'Name', 'required': True,
             'class': 'form-control'})
        self.fields['reference'].widget.attrs.update(
            {'placeholder': 'reference', 'required': True,
             'class': 'form-control'})
        self.fields['order'].widget.attrs.update(
            {'placeholder': 'order', 'required': True,
             'class': 'form-control'})
        self.fields['style'].widget.attrs.update(
            {'placeholder': 'Style', 'class': 'form-control'})
        self.fields['match'].widget.attrs.update(
            {'placeholder': 'Match', 'class': 'form-control'})

    class Meta:
        model = MenuItem
        fields = "__all__"


class MenuPermissionsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'Name', 'required': True,
             'class': 'form-control'})

    class Meta:
        model = MenuPermissions
        fields = "__all__"


class TeamMenuForm(forms.ModelForm):
    team = forms.ModelChoiceField(
        queryset=Team.objects.all(), empty_label=None, widget=forms.Select(
            attrs={'placeholder': 'Team', 'required': True, 'class': 'form-control'}))
    menu = forms.ModelChoiceField(
        queryset=Menu.objects.all(), empty_label=None, widget=forms.Select(
            attrs={'placeholder': 'Menu', 'required': True, 'class': 'form-control'}))
    permissions_menu = forms.ModelMultipleChoiceField(
        queryset=MenuPermissions.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['permissions_menu'].widget.attrs.update(
            {'placeholder': 'Permissions Menu', 'class': 'styled'})
        if self.instance.id:
            self.fields['team'].queryset = Team.objects.filter(pk=self.instance.team.id)
            self.fields['menu'].queryset = Menu.objects.filter(pk=self.instance.menu.id)

    class Meta:
        model = TeamMenu
        fields = "__all__"

    def save(self, *arg, **kwargs):
        team_menu = super().save(*arg, **kwargs)
        return team_menu


class TeamMenuItemForm(forms.ModelForm):
    menu_item = forms.ModelChoiceField(
        queryset=MenuItem.objects.all(), empty_label=None, widget=forms.Select(
            attrs={'placeholder': 'Menu item', 'required': True,
                   'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['team_menu'].widget.attrs.update(
            {'placeholder': 'Team Menu', 'class': 'form-control'})
        self.fields['menu_item'].widget.attrs.update(
            {'placeholder': 'Menu Item', 'class': 'form-control'})

        if self.instance.id:
            self.fields['menu_item'].queryset = MenuItem.current.filter(menu=self.instance.team_menu.menu)

    class Meta:
        model = TeamMenuItem
        fields = "__all__"

    def save(self, *arg, **kwargs):
        team_menu_item = super().save(*arg, **kwargs)
        return team_menu_item

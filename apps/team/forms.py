from django import forms

from .models import Module, Team


class ModuleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'Name', 'required': True,
             'class': 'form-control'})
        # self.fields['current_status'].widget.attrs.update(
        #     {'placeholder': 'Current Status', 'required': True,
        #      'class': 'form-control'})

    class Meta:
        model = Module
        fields = "__all__"


class TeamForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['current_status'].widget.attrs.update(
        #     {'placeholder': 'status', 'required': True,
        #      'class': 'form-control'})
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'Name', 'required': True,
             'class': 'form-control'})
        self.fields['module'].widget.attrs.update(
            {'placeholder': 'Module', 'required': True,
             'class': 'form-control listbox-custom-text'})

    class Meta:
        model = Team
        fields = "__all__"

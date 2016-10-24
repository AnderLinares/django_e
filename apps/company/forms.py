from django import forms

from core.utils.clearable_fileinput import CustomClearableFileInput
from .models import Organization, Subsidiary, Correlative


class OrganizationForm(forms.ModelForm):
    logo_organization = forms.ImageField(widget=CustomClearableFileInput, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['business_name'].widget.attrs.update(
            {'placeholder': 'Business Name', 'required': True,
             'class': 'form-control'})
        self.fields['document_type'].widget.attrs.update(
            {'placeholder': 'Document Type', 'required': True,
             'class': 'form-control'})
        self.fields['document_number'].widget.attrs.update(
            {'placeholder': 'Document Number', 'required': True,
             'class': 'form-control'})
        self.fields['address'].widget.attrs.update(
            {'placeholder': 'Address', 'class': 'form-control'})
        self.fields['logo_organization'].widget.attrs.update(
            {'placeholder': 'Logo', 'class': 'file-styled'})
        self.fields['phone'].widget.attrs.update(
            {'placeholder': 'Phone', 'class': 'form-control'})
        self.fields['mobile_phone'].widget.attrs.update(
            {'placeholder': 'Mobile Phone', 'class': 'form-control'})

    class Meta:
        model = Organization
        fields = "__all__"


class SubsidiaryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['organization'].widget.attrs.update(
            {'placeholder': 'Organization', 'required': True,
             'class': 'form-control'})
        self.fields['subsidiary_name'].widget.attrs.update(
            {'placeholder': 'Subsidiary Name', 'required': True,
             'class': 'form-control'})
        self.fields['store_local'].widget.attrs.update(
            {'placeholder': 'Store Local', 'required': True,
             'class': 'form-control'})
        self.fields['representative'].widget.attrs.update(
            {'placeholder': 'Representative', 'required': True,
             'class': 'form-control'})
        self.fields['address'].widget.attrs.update(
            {'placeholder': 'Address', 'class': 'form-control'})
        self.fields['phone'].widget.attrs.update(
            {'placeholder': 'Phone', 'class': 'form-control'})
        self.fields['mobile_phone'].widget.attrs.update(
            {'placeholder': 'Mobile Phone', 'class': 'form-control'})

    class Meta:
        model = Subsidiary
        fields = "__all__"


class CorrelativeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['organization'].widget.attrs.update(
            {'placeholder': 'Organization', 'required': True,
             'class': 'form-control'})
        self.fields['type_document'].widget.attrs.update(
            {'placeholder': 'Type Document', 'required': True,
             'class': 'form-control'})
        self.fields['prefix'].widget.attrs.update(
            {'placeholder': 'Prefix', 'class': 'form-control'})
        self.fields['postfix'].widget.attrs.update(
            {'placeholder': 'Postfix', 'class': 'form-control'})
        self.fields['format'].widget.attrs.update(
            {'placeholder': 'Format', 'class': 'form-control'})
        self.fields['initial'].widget.attrs.update(
            {'placeholder': 'Initial', 'class': 'form-control'})
        self.fields['increment'].widget.attrs.update(
            {'placeholder': 'Increment', 'class': 'form-control'})
        self.fields['final'].widget.attrs.update(
            {'placeholder': 'Final', 'class': 'form-control'})
        self.fields['actual'].widget.attrs.update(
            {'placeholder': 'Actual', 'class': 'form-control'})

        organization_id = self.data.get("organization", None)

        if self.instance.id:
            self.fields['subsidiary'].queryset = Subsidiary.objects.filter(
                organization=self.instance.organization)
        else:
            self.fields['subsidiary'] = forms.ChoiceField(choices=(('', '----------'),))

            if organization_id:
                self.fields['subsidiary'] = forms.ModelChoiceField(
                    queryset=Subsidiary.objects.filter(organization=organization_id))

        self.fields['subsidiary'].widget.attrs.update(
            {'placeholder': 'Subsidiary', 'required': True,
             'class': 'form-control'})

    class Meta:
        model = Correlative
        fields = "__all__"

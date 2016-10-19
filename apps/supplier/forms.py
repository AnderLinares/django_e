from django import forms

from .models import Supplier, SupplierSubsidiary, SupplierProduct


class SupplierForm(forms.ModelForm):
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
        self.fields['home_phone'].widget.attrs.update(
            {'placeholder': 'Home Phone', 'required': True,
             'class': 'form-control'})
        self.fields['mobile_phone'].widget.attrs.update(
            {'placeholder': 'Mobile Phone', 'class': 'form-control'})
        self.fields['address'].widget.attrs.update(
            {'placeholder': 'Address', 'class': 'form-control'})
        self.fields['contact'].widget.attrs.update(
            {'placeholder': 'Contact', 'class': 'form-control'})
        self.fields['phone_contact'].widget.attrs.update(
            {'placeholder': 'Phone Contact', 'class': 'form-control'})

    class Meta:
        model = Supplier
        fields = "__all__"


class SupplierSubsidiaryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['supplier'].widget.attrs.update(
            {'placeholder': 'Supplier', 'class': 'form-control'})
        self.fields['subsidiary'].widget.attrs.update(
            {'placeholder': 'Subsidiary', 'class': 'listbox-custom-text'})

    class Meta:
        model = SupplierSubsidiary
        fields = "__all__"


class SupplierProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['supplier'].widget.attrs.update(
            {'placeholder': 'Supplier', 'class': 'form-control'})
        self.fields['product'].widget.attrs.update(
            {'placeholder': 'Product', 'class': 'listbox-custom-text'})

    class Meta:
        model = SupplierProduct
        fields = "__all__"

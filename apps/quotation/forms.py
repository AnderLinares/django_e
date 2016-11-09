import datetime

from django import forms

from apps.customer.models import User
from apps.product.models import ProductCategory, Product
from core.models import HandWorkCategory, HandWork
from .models import QuotationStore, QuotationStoreDetail, QuotationMaintenance


class QuotationStoreForm(forms.ModelForm):
    applicant = forms.ModelChoiceField(
        queryset=User.objects.all(), empty_label=None, widget=forms.Select(
            attrs={'placeholder': 'User', 'required': True, 'class': 'form-control'}))
    category = forms.ModelChoiceField(
        queryset=ProductCategory.objects.all(), widget=forms.Select(
            attrs={'class': 'form-control'}), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        initial = kwargs.get('initial', None)
        self.fields['code_qt_store'].widget.attrs.update(
            {'placeholder': 'Code Quotation', 'class': 'form-control'})
        self.fields['supplier'].widget.attrs.update(
            {'placeholder': 'Supplier', 'class': 'form-control'})
        self.fields['applicant'].widget.attrs.update(
            {'placeholder': 'Applicant', 'class': 'form-control'})
        self.fields['date'].widget.attrs.update(
            {'placeholder': 'Date', 'class': 'form-control datepicker'})
        if initial:
            self.fields['code_qt_store'].initial = initial["code_qt"]["current_aggregate_format"]
            self.fields['code_qt_store'].widget.attrs.update({'readonly': True})
            self.fields['applicant'].queryset = User.objects.filter(pk=initial["user"].id)
            self.fields['date'].initial = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d")

    def save(self, commit=True):
        qt_store = super().save(commit=False)
        if commit:
            qt_store.save()
        return qt_store

    class Meta:
        model = QuotationStore
        fields = "__all__"


class QuotationStoreDetailForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].widget.attrs.update(
            {'placeholder': 'Product', 'class': 'form-control'})
        self.fields['quantity'].widget.attrs.update(
            {'placeholder': 'Quantity', 'class': 'form-control'})

    class Meta:
        model = QuotationStoreDetail
        fields = "__all__"

    def save(self, commit=True):
        return super().save(commit)


class QuotationMaintenanceForm(forms.ModelForm):
    applicant = forms.ModelChoiceField(
        queryset=User.objects.all(), empty_label=None, widget=forms.Select(
            attrs={'placeholder': 'User', 'required': True, 'class': 'form-control'}))
    frm_product_category = forms.ModelChoiceField(
        queryset=ProductCategory.objects.all(), required=False)
    frm_product = forms.ModelChoiceField(
        queryset=Product.objects.all(), required=False)
    frm_handwork_category = forms.ModelChoiceField(
        queryset=HandWorkCategory.objects.all(), required=False)
    frm_handwork = forms.ModelChoiceField(
        queryset=HandWork.objects.all(), required=False)
    frm_igv_tax = forms.CharField(required=False, widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        initial = kwargs.get('initial', None)
        self.fields['code_qt_maintenance'].widget.attrs.update(
            {'placeholder': 'Code COM.', 'class': 'form-control'})
        self.fields['date'].widget.attrs.update(
            {'placeholder': 'Date', 'class': 'form-control datepicker'})
        self.fields['client'].widget.attrs.update(
            {'placeholder': 'Client', 'class': 'form-control'})
        self.fields['vehicle'].widget.attrs.update(
            {'placeholder': 'Vehicle', 'class': 'form-control'})
        self.fields['igv_total'].widget.attrs.update(
            {'placeholder': 'Igv Tax', 'class': 'form-control'})
        self.fields['sub_total'].widget.attrs.update(
            {'placeholder': 'Sub Total', 'class': 'form-control'})
        self.fields['total_paid'].widget.attrs.update(
            {'placeholder': 'Total Paid', 'class': 'form-control'})
        self.fields['frm_product_category'].widget.attrs.update({'class': 'form-control'})
        self.fields['frm_product'].widget.attrs.update({'class': 'form-control'})
        self.fields['frm_handwork_category'].widget.attrs.update({'class': 'form-control'})
        self.fields['frm_handwork'].widget.attrs.update({'class': 'form-control'})
        if initial:
            self.fields['code_qt_maintenance'].initial = initial["code_qt"]["current_aggregate_format"]
            self.fields['code_qt_maintenance'].widget.attrs.update({'readonly': True})
            self.fields['applicant'].queryset = User.objects.filter(pk=initial["user"].id)
            self.fields['date'].initial = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d")
            self.fields['frm_igv_tax'].initial = initial["igv_tax"]

    class Meta:
        model = QuotationMaintenance
        fields = "__all__"

    def save(self, commit=True):
        qt_maintenance = super().save(commit=False)
        if commit:
            qt_maintenance.save()
        return qt_maintenance

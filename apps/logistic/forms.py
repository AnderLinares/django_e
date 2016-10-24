from django import forms
import datetime

from apps.customer.models import User
from apps.product.models import ProductCategory
from .models import (
    PurchaseOrder, PurchaseOrderDetail
)


class PurchaseOrderForm(forms.ModelForm):
    applicant = forms.ModelChoiceField(
        queryset=User.objects.all(), empty_label=None, widget=forms.Select(
            attrs={'placeholder': 'User', 'required': True, 'class': 'form-control'}))
    category = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        initial = kwargs.get('initial', None)
        self.fields['code_po_store'].widget.attrs.update(
            {'placeholder': 'Code Purchase Order', 'class': 'form-control'})
        self.fields['supplier'].widget.attrs.update(
            {'placeholder': 'Supplier', 'class': 'form-control'})
        self.fields['applicant'].widget.attrs.update(
            {'placeholder': 'Applicant', 'class': 'form-control'})
        self.fields['currency'].widget.attrs.update(
            {'placeholder': 'Currency', 'class': 'form-control'})
        self.fields['purchase_condition'].widget.attrs.update(
            {'placeholder': 'Purchase Condition', 'class': 'form-control'})
        self.fields['date'].widget.attrs.update(
            {'placeholder': 'Date', 'class': 'form-control datepicker'})
        self.fields['igv_tax'].widget.attrs.update(
            {'placeholder': 'Igv tax', 'class': 'form-control', 'readonly': True})
        self.fields['igv_total'].widget.attrs.update(
            {'placeholder': 'Igv Total', 'class': 'form-control', 'readonly': True})
        self.fields['sub_total'].widget.attrs.update(
            {'placeholder': 'Sub total', 'class': 'form-control', 'readonly': True})
        self.fields['total_paid'].widget.attrs.update(
            {'placeholder': 'Total paid', 'class': 'form-control', 'readonly': True})

        self.fields['category'] = forms.ModelChoiceField(
            queryset=ProductCategory.objects.all(), widget=forms.Select(
                attrs={'class': 'form-control'}), required=False)

        if initial:
            self.fields['code_po_store'].initial = initial["code_po"]["current_aggregate_format"]
            self.fields['code_po_store'].widget.attrs.update({'readonly': True})
            self.fields['applicant'].queryset = User.objects.filter(pk=initial["user"].id)
            self.fields['date'].initial = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d")
            self.fields['igv_tax'].initial = initial["igv_tax"]

    def save(self, commit=True):
        po_store = super().save(commit=False)
        if commit:
            po_store.save()
        return po_store

    class Meta:
        model = PurchaseOrder
        fields = "__all__"


class PurchaseOrderDetailForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].widget.attrs.update(
            {'placeholder': 'Product', 'class': 'form-control'})
        self.fields['description'].widget.attrs.update(
            {'placeholder': 'Description', 'class': 'form-control'})
        self.fields['quantity'].widget.attrs.update(
            {'placeholder': 'Quantity', 'class': 'form-control'})
        self.fields['unit_price'].widget.attrs.update(
            {'placeholder': 'Unit Price', 'class': 'form-control', 'readonly': True})
        self.fields['discount'].widget.attrs.update(
            {'placeholder': 'Discount', 'class': 'form-control'})
        self.fields['amount_price'].widget.attrs.update(
            {'placeholder': 'Amount Price', 'class': 'form-control', 'readonly': True})

    class Meta:
        model = PurchaseOrderDetail
        fields = "__all__"

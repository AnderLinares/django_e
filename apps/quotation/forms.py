import datetime

from django import forms

from apps.customer.models import User
from apps.product.models import ProductCategory
from .models import QuotationStore, QuotationStoreDetail


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

    # def save(self, *arg, commit=True):
    #     quotation_store = super().save(commit=False)
    #     quotation_store.save()
    #     return quotation_store



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

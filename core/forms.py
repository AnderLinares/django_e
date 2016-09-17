from django import forms

from .models import (
    Organization, Subsidiary, Currency, ExchangeRate, UnitMeasurement
)


class CurrencyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sk'].widget.attrs.update(
            {'placeholder': 'Sk', 'class': 'form-control'})
        self.fields['code'].widget.attrs.update(
            {'placeholder': 'code', 'class': 'form-control'})
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'Name', 'class': 'form-control'})
        self.fields['is_fund'].widget.attrs.update(
            {'placeholder': 'is_fund', 'class': 'form-control'})
        self.fields['is_complimentary'].widget.attrs.update(
            {'placeholder': 'is_complimentary', 'class': 'form-control'})
        self.fields['is_metal'].widget.attrs.update(
            {'placeholder': 'is_metal', 'class': 'form-control'})

    class Meta:
        model = Currency
        fields = ["sk", "code", "name", "is_fund", "is_complimentary", "is_metal"]


class ExchangeRateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['currency'].widget.attrs.update(
            {'placeholder': 'Currency', 'class': 'form-control'})
        self.fields['exchange_rate'].widget.attrs.update(
            {'placeholder': 'Exchange rate', 'class': 'form-control'})
        self.fields['start_date'].widget.attrs.update(
            {'placeholder': 'Start date', 'class': 'form-control'})
        self.fields['end_date'].widget.attrs.update(
            {'placeholder': 'End date', 'class': 'form-control'})

    class Meta:
        model = ExchangeRate
        fields = ["currency", "exchange_rate", "start_date", "end_date"]


class OrganizationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'Name', 'class': 'form-control'})
        self.fields['reason_social'].widget.attrs.update(
            {'placeholder': 'Reason social', 'class': 'form-control'})
        self.fields['initial_exercise'].widget.attrs.update(
            {'placeholder': 'Initial exercise', 'class': 'form-control'})
        self.fields['final_exercise'].widget.attrs.update(
            {'placeholder': 'Final exercise ', 'class': 'form-control'})
        self.fields['nit'].widget.attrs.update(
            {'placeholder': 'Nit', 'class': 'form-control'})
        self.fields['legal_representative'].widget.attrs.update(
            {'placeholder': 'Legal representative', 'class': 'form-control'})
        self.fields['accountant'].widget.attrs.update(
            {'placeholder': 'Accountant', 'class': 'form-control'})
        self.fields['register_accountant'].widget.attrs.update(
            {'placeholder': 'Register accountant', 'class': 'form-control'})
        self.fields['address'].widget.attrs.update(
            {'placeholder': 'Address', 'class': 'form-control'})
        self.fields['logo_url'].widget.attrs.update(
            {'placeholder': 'Logo url', 'class': 'form-control'})
        self.fields['primary_currency'].widget.attrs.update(
            {'placeholder': 'Primary currency', 'class': 'form-control'})
        self.fields['phone'].widget.attrs.update(
            {'placeholder': 'Phone', 'class': 'form-control'})
        self.fields['mobile_phone'].widget.attrs.update(
            {'placeholder': 'Mobile phone', 'class': 'form-control'})

    class Meta:
        model = Organization
        fields = ["name", "reason_social", "initial_exercise", "final_exercise", "nit",
                  "legal_representative", "accountant", "register_accountant",
                  "address", "logo_url", "primary_currency", "phone", "mobile_phone"]


class SubsidiaryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['organization'].widget.attrs.update(
            {'placeholder': 'Organization', 'required': True, 'class': 'form-control'})
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'name', 'class': 'form-control'})
        self.fields['address'].widget.attrs.update(
            {'placeholder': 'address', 'class': 'form-control'})
        self.fields['phone'].widget.attrs.update(
            {'placeholder': 'Phone', 'class': 'form-control'})
        self.fields['mobile_phone'].widget.attrs.update(
            {'placeholder': 'Mobile phone', 'class': 'form-control'})

    class Meta:
        model = Subsidiary
        fields = ["organization", "name", "address", "phone", "mobile_phone"]


class UnitMeasurementForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type_measurement'].widget.attrs.update(
            {'placeholder': 'Type measurement', 'required': True, 'class': 'form-control'})
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'name', 'class': 'form-control'})
        self.fields['symbol'].widget.attrs.update(
            {'placeholder': 'symbol', 'class': 'form-control'})

    class Meta:
        model = UnitMeasurement
        fields = ["type_measurement", "name", "symbol"]

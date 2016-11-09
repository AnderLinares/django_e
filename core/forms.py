from django import forms

from .models import (
    UnitMeasurement, PurchaseCondition, VehicleInventory,
    VehicleEnrollment, VehicleBrand, VehicleModel, VehicleFuel,
    ProductBrand, ProductModel,
    Currency, ExchangeRate, Service, Store, Person,
    LabourCategory, Labour,
    ConsultService, HandWorkCategory, HandWork)


class HandWorkCategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'Name', 'required': True,
             'class': 'form-control'})

    class Meta:
        model = HandWorkCategory
        fields = "__all__"


class HandWorkForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['handwork_category'].widget.attrs.update(
            {'placeholder': 'handwork category', 'required': True,
             'class': 'form-control'})
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'Name', 'required': True,
             'class': 'form-control'})
        self.fields['currency'].widget.attrs.update(
            {'placeholder': 'currency', 'required': True,
             'class': 'form-control'})
        self.fields['price'].widget.attrs.update(
            {'placeholder': 'price', 'required': True,
             'class': 'form-control'})

    class Meta:
        model = HandWork
        fields = "__all__"


class LabourCategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'Name', 'required': True,
             'class': 'form-control'})

    class Meta:
        model = LabourCategory
        fields = "__all__"


class LabourForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['labour_category'].widget.attrs.update(
            {'placeholder': 'Labour Category', 'required': True,
             'class': 'form-control'})
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'Name', 'required': True,
             'class': 'form-control'})

    class Meta:
        model = Labour
        fields = "__all__"


class UnitMeasurementForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type_measurement'].widget.attrs.update(
            {'placeholder': 'Type measurement', 'required': True,
             'class': 'form-control'})
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'name', 'required': True,
             'class': 'form-control'})
        self.fields['symbol'].widget.attrs.update(
            {'placeholder': 'symbol', 'class': 'form-control'})

    class Meta:
        model = UnitMeasurement
        fields = "__all__"


class VehicleEnrollmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['year'].widget.attrs.update(
            {'placeholder': 'Year', 'required': True,
             'class': 'form-control'})

    class Meta:
        model = VehicleEnrollment
        fields = "__all__"


class VehicleBrandForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'Name', 'required': True,
             'class': 'form-control'})

    class Meta:
        model = VehicleBrand
        fields = "__all__"


class VehicleModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['brand'].widget.attrs.update(
            {'placeholder': 'Brand', 'required': True,
             'class': 'form-control'})
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'Name', 'required': True,
             'class': 'form-control'})

    class Meta:
        model = VehicleModel
        fields = "__all__"


class VehicleFuelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['unit_transport'].widget.attrs.update(
            {'placeholder': 'Unit Transport', 'required': True,
             'class': 'form-control'})
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'Name', 'required': True,
             'class': 'form-control'})

    class Meta:
        model = VehicleFuel
        fields = "__all__"


class VehicleInventoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'Name', 'required': True,
             'class': 'form-control'})

    class Meta:
        model = VehicleInventory
        fields = "__all__"


class PurchaseConditionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'Name', 'required': True,
             'class': 'form-control'})

    class Meta:
        model = PurchaseCondition
        fields = "__all__"


class ProductBrandForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'Name', 'required': True,
             'class': 'form-control'})

    class Meta:
        model = ProductBrand
        fields = "__all__"


class ProductModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['brand'].widget.attrs.update(
            {'placeholder': 'Brand', 'required': True,
             'class': 'form-control'})
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'Name', 'required': True,
             'class': 'form-control'})

    class Meta:
        model = ProductModel
        fields = "__all__"


class CurrencyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sk'].widget.attrs.update(
            {'placeholder': 'Sk', 'required': True,
             'class': 'form-control'})
        self.fields['code'].widget.attrs.update(
            {'placeholder': 'Code', 'required': True,
             'class': 'form-control'})
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'Name', 'required': True,
             'class': 'form-control'})
        self.fields['is_fund'].widget.attrs.update(
            {'placeholder': 'is fund',
             'class': 'styled'})
        self.fields['is_complimentary'].widget.attrs.update(
            {'placeholder': 'is complimentary',
             'class': 'styled'})
        self.fields['is_metal'].widget.attrs.update(
            {'placeholder': 'is metal',
             'class': 'styled'})

    class Meta:
        model = Currency
        fields = "__all__"


class ExchangeRateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['currency'].widget.attrs.update(
            {'placeholder': 'currency', 'required': True,
             'class': 'form-control'})
        self.fields['exchange_rate'].widget.attrs.update(
            {'placeholder': 'exchange_rate', 'required': True,
             'class': 'form-control'})
        self.fields['start_date'].widget.attrs.update(
            {'placeholder': 'start_date', 'class': 'form-control datepicker'})
        self.fields['end_date'].widget.attrs.update(
            {'placeholder': 'end_date', 'class': 'form-control datepicker'})

    class Meta:
        model = ExchangeRate
        fields = "__all__"


class ServiceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'Name', 'required': True,
             'class': 'form-control'})

    class Meta:
        model = Service
        fields = "__all__"


class StoreForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'Name', 'required': True,
             'class': 'form-control'})
        self.fields['is_principal'].widget.attrs.update(
            {'placeholder': 'is_principal', 'class': 'styled'})

    class Meta:
        model = Store
        fields = "__all__"


class PersonForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {'placeholder': 'First name', 'required': True,
             'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update(
            {'placeholder': 'Last_name', 'class': 'form-control'})
        self.fields['email'].widget.attrs.update(
            {'placeholder': 'Email', 'required': True,
             'class': 'form-control'})
        self.fields['address'].widget.attrs.update(
            {'placeholder': 'Address', 'class': 'form-control'})
        self.fields['home_phone'].widget.attrs.update(
            {'placeholder': 'Home phone', 'required': True,
             'class': 'form-control'})
        self.fields['mobile_phone'].widget.attrs.update(
            {'placeholder': 'Mobile phone', 'class': 'form-control'})
        self.fields['document_type'].widget.attrs.update(
            {'placeholder': 'Document type', 'required': True,
             'class': 'form-control'})
        self.fields['document_number'].widget.attrs.update(
            {'placeholder': 'Document number', 'class': 'form-control'})
        self.fields['person_tribute'].widget.attrs.update(
            {'placeholder': 'Person Tribute', 'required': True,
             'class': 'form-control'})
        self.fields['is_client'].widget.attrs.update(
            {'placeholder': 'client', 'class': 'styled'})
        self.fields['is_taxi_driver'].widget.attrs.update(
            {'placeholder': 'taxi driver', 'class': 'styled'})

    class Meta:
        model = Person
        fields = "__all__"


class ConsultServiceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'Name', 'required': True,
             'class': 'form-control'})
        self.fields['url_service'].widget.attrs.update(
            {'placeholder': 'Url Service', 'required': True,
             'class': 'form-control'})
        self.fields['description'].widget.attrs.update(
            {'placeholder': 'Description', 'required': True,
             'class': 'form-control'})

    class Meta:
        model = ConsultService
        fields = "__all__"

from django import forms

from .constants import CODE_STATUS_AVAILABLE, CODE_STATUS_NULL
from .models import Brand, Labour, TypeJob, Vehicle, Quotation, QuotationDetail


class BrandForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'Name', 'required': True,
             'class': 'form-control'})

    class Meta:
        model = Brand
        fields = ['name']


class LabourForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type_job'].widget.attrs.update(
            {'required': True, 'class': 'form-control'})
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'Name', 'required': True,
             'class': 'form-control'})
        self.fields['cost_price'].widget.attrs.update(
            {'placeholder': 'Cost Price', 'required': True,
             'class': 'form-control'})
        self.fields['sale_price'].widget.attrs.update(
            {'placeholder': 'Sale Price', 'required': True,
             'class': 'form-control'})

    class Meta:
        model = Labour
        fields = ["type_job", "name", "cost_price", "sale_price"]


class TypeJobForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'Name', 'required': True,
             'class': 'form-control'})

    class Meta:
        model = TypeJob
        fields = ['name']


class VehicleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type_vehicle'].widget.attrs.update(
            {'placeholder': 'Type vehicle', 'required': True, 'class': 'form-control'})
        self.fields['brand'].widget.attrs.update(
            {'placeholder': 'brand', 'required': True, 'class': 'form-control'})
        self.fields['plaque'].widget.attrs.update(
            {'placeholder': 'Plaque', 'class': 'form-control'})
        self.fields['model'].widget.attrs.update(
            {'placeholder': 'Model', 'class': 'form-control'})
        self.fields['year_car'].widget.attrs.update(
            {'placeholder': 'Year car', 'class': 'form-control'})
        self.fields['vin'].widget.attrs.update(
            {'placeholder': 'VIN', 'class': 'form-control'})
        self.fields['color'].widget.attrs.update(
            {'placeholder': 'Color', 'class': 'colorpicker form-control'})
        self.fields['serie_motor'].widget.attrs.update(
            {'placeholder': 'serie_motor', 'class': 'form-control'})
        self.fields['soat'].widget.attrs.update(
            {'placeholder': 'soat', 'class': 'form-control'})
        self.fields['expiration_soat'].widget.attrs.update(
            {'placeholder': 'expiration_soat', 'class': 'form-control'})
        self.fields['poliza'].widget.attrs.update(
            {'placeholder': 'Poliza', 'class': 'form-control'})
        self.fields['expiration_poliza'].widget.attrs.update(
            {'placeholder': 'Expiration poliza', 'class': 'form-control mydatepicker'})
        self.fields['technical_review'].widget.attrs.update(
            {'placeholder': 'Technical review', 'class': 'form-control'})
        self.fields['expiration_technical_review'].widget.attrs.update(
            {'placeholder': 'Expiration technical review', 'class': 'form-control mydatepicker'})
        self.fields['opacity_test'].widget.attrs.update(
            {'placeholder': 'Opacity test', 'class': 'form-control'})
        self.fields['expiration_opacity_test'].widget.attrs.update(
            {'placeholder': 'Expiration opacity test', 'class': 'form-control'})
        self.fields['farenet_test'].widget.attrs.update(
            {'placeholder': 'Farenet test', 'class': 'form-control'})
        self.fields['expiration_farenet_test'].widget.attrs.update(
            {'placeholder': 'Expiration farenet test', 'class': 'form-control'})
        self.fields['is_flotilla'].widget.attrs.update(
            {'placeholder': 'Is flotilla', 'class': 'form-control'})

    class Meta:
        model = Vehicle
        fields = ["type_vehicle", "brand", "plaque", "model",
                  "year_car", "vin", "color", "serie_motor", "soat", "expiration_soat",
                  "poliza", "expiration_poliza", "technical_review",
                  "expiration_technical_review", "opacity_test", "expiration_opacity_test",
                  "farenet_test", "expiration_farenet_test", "is_flotilla"]

    def save(self, user=None, commit=True):
        vehicle = super().save(commit=False)
        if not commit:
            if self.cleaned_data["is_flotilla"]:
                vehicle.status_vehicle = CODE_STATUS_AVAILABLE
            else:
                vehicle.status_vehicle = CODE_STATUS_NULL
            vehicle.subsidiary = user.get_subsidiary()
            vehicle.save()
        else:
            vehicle.save()
        return vehicle


class QuotationForm(forms.ModelForm):
    sale_price = forms.DecimalField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['client'].widget.attrs.update(
            {'placeholder': 'Client', 'required': True, 'class': 'typeahead form-control'})
        self.fields['vehicle'].widget.attrs.update(
            {'placeholder': 'Vehicle', 'required': True, 'class': 'form-control'})
        self.fields['labour'].widget.attrs.update(
            {'placeholder': 'Labour', 'required': True, 'class': 'form-control'})
        # self.fields['labour'].choices = [('', '----------')] + [(lang.id, lang.name) for lang in Labour.objects.all()]
        self.fields['sale_price'].widget.attrs.update(
            {'placeholder': 'Sale price', 'class': 'form-control'})
        self.fields['currency'].widget.attrs.update(
            {'placeholder': 'Currency', 'class': 'form-control'})
        self.fields['igv_tax'].widget.attrs.update(
            {'placeholder': 'igv tax', 'class': 'form-control'})
        self.fields['sub_total'].widget.attrs.update(
            {'placeholder': 'Sub total', 'class': 'form-control'})
        self.fields['total_paid'].widget.attrs.update(
            {'placeholder': 'Total paid', 'class': 'form-control'})
        self.fields['current_date'].widget.attrs.update(
            {'placeholder': 'Current date', 'class': 'form-control'})


    class Meta:
        model = Quotation
        fields = ["client", "labour", "vehicle", "currency", "igv_tax",
                  "sub_total", "total_paid", "current_date"]


class QuotationDetailForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quotation'].widget.attrs.update(
            {'placeholder': 'Quotation', 'class': 'form-control'})
        self.fields['description'].widget.attrs.update(
            {'placeholder': 'Description', 'class': 'form-control'})
        self.fields['quantity'].widget.attrs.update(
            {'placeholder': 'Quantity', 'class': 'form-control'})
        self.fields['unit_price'].widget.attrs.update(
            {'placeholder': 'Unit price', 'class': 'form-control'})
        self.fields['amount_price'].widget.attrs.update(
            {'placeholder': 'Amount price', 'class': 'form-control'})

    class Meta:
        model = QuotationDetail
        fields = ["quotation", "description", "quantity", "unit_price", "amount_price"]

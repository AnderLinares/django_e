from django import forms

from core.models import VehicleModel
from core.utils.clearable_fileinput import CustomClearableFileInput
from .models import Vehicle, VehicleDetail, VehicleImage


class VehicleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['unit_transport'].widget.attrs.update(
            {'placeholder': 'Unit Transport', 'required': True,
             'class': 'form-control'})
        self.fields['brand'].widget.attrs.update(
            {'placeholder': 'Brand', 'required': True,
             'class': 'form-control'})
        self.fields['year_car'].widget.attrs.update(
            {'placeholder': 'Year Car', 'required': True,
             'class': 'form-control'})
        self.fields['plaque'].widget.attrs.update(
            {'placeholder': 'Plaque', 'required': True,
             'class': 'form-control'})
        self.fields['color'].widget.attrs.update(
            {'placeholder': 'Color', 'required': True,
             'class': 'form-control colorpicker-basic'})
        self.fields['type_vehicle'].widget.attrs.update(
            {'placeholder': 'Type Vehicle', 'required': True,
             'class': 'form-control'})

        brand_id = self.data.get("brand", None)
        if self.instance.id:
            self.fields['model'].queryset = VehicleModel.objects.filter(
                brand=self.instance.brand)
        else:
            self.fields['model'] = forms.ChoiceField(choices=(('', '----------'),))
            if brand_id:
                self.fields['model'] = forms.ModelChoiceField(
                    queryset=VehicleModel.objects.filter(brand=brand_id))

        self.fields['model'].widget.attrs.update(
            {'placeholder': 'Model', 'required': True,
             'class': 'form-control'})

    class Meta:
        model = Vehicle
        fields = "__all__"


class VehicleDetailForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['serie_motor'].widget.attrs.update(
            {'placeholder': 'Serie Motor', 'class': 'form-control'})
        self.fields['soat'].widget.attrs.update(
            {'placeholder': 'Soat', 'class': 'form-control'})
        self.fields['expiration_soat'].widget.attrs.update(
            {'placeholder': 'Expiration Soat', 'class': 'form-control datepicker'})
        self.fields['poliza'].widget.attrs.update(
            {'placeholder': 'Poliza', 'class': 'form-control'})
        self.fields['expiration_poliza'].widget.attrs.update(
            {'placeholder': 'Expiration Poliza', 'class': 'form-control datepicker'})
        self.fields['technical_review'].widget.attrs.update(
            {'placeholder': 'Technical Review', 'class': 'form-control'})
        self.fields['expiration_technical_review'].widget.attrs.update(
            {'placeholder': 'Expiration Technical Review', 'class': 'form-control datepicker'})
        self.fields['opacity_test'].widget.attrs.update(
            {'placeholder': 'Opacity Test', 'class': 'form-control'})
        self.fields['expiration_opacity_test'].widget.attrs.update(
            {'placeholder': 'Expiration Opacity Test', 'class': 'form-control datepicker'})
        self.fields['farenet_test'].widget.attrs.update(
            {'placeholder': 'Farenet Test', 'class': 'form-control'})
        self.fields['expiration_farenet_test'].widget.attrs.update(
            {'placeholder': 'Expiration Farenet Test', 'class': 'form-control datepicker'})

    class Meta:
        model = VehicleDetail
        fields = ["serie_motor", "soat", "expiration_soat", "poliza", "expiration_poliza",
                  "technical_review", "expiration_technical_review", "opacity_test",
                  "expiration_opacity_test", "farenet_test", "expiration_farenet_test"]

    def save(self, vehicle=None, commit=True):
        vehicle_detail = super().save(commit=False)
        if vehicle:
            vehicle_detail.vehicle = vehicle
        vehicle_detail.save()
        return vehicle_detail


class VehicleImageForm(forms.ModelForm):
    logo_vehicle = forms.ImageField(widget=CustomClearableFileInput, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['logo_vehicle'].widget.attrs.update(
            {'placeholder': 'Image', 'class': 'form-control'})

    class Meta:
        model = VehicleImage
        fields = "__all__"


from django import forms

from apps.customer.models import User
from apps.product.models import Product
from apps.vehicle.models import VehicleDetail, Vehicle
from core import constants as core_constants
from core.models import VehicleInventory, Labour, Person
from .models import (
    ActDeliveryVehicle, InventoryDeliveryVehicle, ObservationDeliveryVehicle,
    WorkAssignment, WorkAssignmentDetail, WorkAssignmentStore,
    RequisitionStore, RequisitionStoreDetail)


class ActDeliveryVehicleForm(forms.ModelForm):
    frm_brand = forms.CharField(
        required=False, widget=forms.TextInput(
            attrs={"readonly": True, "disabled": True, 'class': 'form-control'}))
    frm_model = forms.CharField(
        required=False, widget=forms.TextInput(
            attrs={"readonly": True, "disabled": True, 'class': 'form-control'}))
    frm_color = forms.CharField(
        required=False, widget=forms.TextInput(
            attrs={"readonly": True, "disabled": True, 'class': 'form-control'}))
    frm_service_taller = forms.CharField(required=False, widget=forms.HiddenInput())
    frm_vehicle = forms.CharField(required=False, widget=forms.HiddenInput())
    frm_following_maintenance = forms.CharField(required=False, widget=forms.HiddenInput())
    frm_person = forms.CharField(required=False, widget=forms.HiddenInput())
    applicant = forms.ModelChoiceField(
        queryset=User.objects.all(), empty_label=None, widget=forms.Select(
            attrs={'required': True, 'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        initial = kwargs.get('initial', None)
        self.fields['code_adv_taller'].widget.attrs.update(
            {'placeholder': 'Code ADV', 'class': 'form-control'})
        self.fields['service_taller'].widget.attrs.update(
            {'placeholder': 'Service Taller', 'required': True, 'class': 'form-control'})
        self.fields['type_solicitude_entry'].widget.attrs.update(
            {'placeholder': 'Type Solicitude', 'required': True, 'class': 'form-control'})
        self.fields['vehicle'].widget.attrs.update(
            {'placeholder': 'Vehicle', 'required': True, 'class': 'form-control'})
        self.fields['person'].widget.attrs.update(
            {'placeholder': 'Person', 'required': True, 'class': 'form-control'})
        self.fields['date_entry'].widget.attrs.update(
            {'placeholder': 'Date Entry', 'required': True, 'class': 'form-control datepicker'})
        self.fields['hour_entry'].widget.attrs.update(
            {'placeholder': 'Hour Entry', 'required': True, 'class': 'form-control pickatime'})
        self.fields['km_entry'].widget.attrs.update(
            {'placeholder': 'Km Entry', 'required': True, 'class': 'form-control'})
        self.fields['fuel_entry'].widget.attrs.update(
            {'placeholder': 'Fuel Entry', 'required': True, 'class': 'form-control'})
        self.fields['following_maintenance'].widget.attrs.update(
            {'placeholder': 'following maintenance', 'required': True, 'class': 'form-control datepicker'})
        self.fields['frm_color'].widget.attrs.update(
            {'placeholder': 'Color', 'class': 'form-control colorpicker-disabled', "data-preferred-format": "hex"})
        self.fields['taxi_driver_entry'].widget.attrs.update(
            {'placeholder': 'Taxi Driver Entry', 'required': True, 'class': 'form-control'})
        self.fields['type_solicitude_entry'].choices = core_constants.SELECT_DEFAULT_ + [
            core_constants.SIS_TALLER_SOLICITUDE_ENTRY_STRING]

        self.fields['km_exit'].required = False
        self.fields['taxi_driver_exit'].required = False
        self.fields['fuel_exit'].required = False
        self.fields['type_solicitude_exit'].required = False

        if initial:
            self.fields['code_adv_taller'].initial = initial["code_adv"]["current_aggregate_format"]
            self.fields['code_adv_taller'].widget.attrs.update({'readonly': True})
            self.fields['applicant'].queryset = User.objects.filter(pk=initial["user"].id)

        if self.instance.id:
            self.fields["service_taller"].widget = forms.HiddenInput()
            self.fields['frm_service_taller'].widget = forms.TextInput(
                attrs={"class": "form-control", "disabled": True})
            self.fields['frm_service_taller'].initial = self.instance.get_service_taller_display()

            self.fields['type_solicitude_entry'].widget = forms.HiddenInput()
            self.fields['type_solicitude_exit'].widget = forms.Select(attrs={"class": "form-control", "required": True})
            self.fields['type_solicitude_exit'].choices = core_constants.SELECT_DEFAULT_ + [
                core_constants.SIS_TALLER_SOLICITUDE_EXIT_STRING]

            self.fields['vehicle'].widget = forms.HiddenInput()
            self.fields['frm_vehicle'].widget = forms.TextInput(attrs={"class": "form-control", "disabled": True})
            self.fields['frm_vehicle'].initial = self.instance.vehicle

            self.fields['person'].widget = forms.HiddenInput()
            self.fields['frm_person'].widget = forms.TextInput(attrs={"class": "form-control", "disabled": True})
            self.fields['frm_person'].initial = self.instance.person

            self.fields['following_maintenance'].widget = forms.HiddenInput()
            self.fields['frm_following_maintenance'].widget = forms.TextInput(
                attrs={"class": "form-control", "disabled": True})
            self.fields['frm_following_maintenance'].initial = self.instance.following_maintenance

            self.fields['taxi_driver_entry'].widget = forms.HiddenInput()
            self.fields['taxi_driver_exit'].widget.attrs.update({'required': True, 'class': 'form-control'})

            self.fields['fuel_entry'].widget = forms.HiddenInput()
            self.fields['fuel_exit'].widget.attrs.update({'required': True, 'class': 'form-control'})

            self.fields['km_entry'].widget = forms.HiddenInput()
            self.fields['km_exit'].widget.attrs.update({'required': True, 'class': 'form-control'})

            self.fields['date_entry'].widget = forms.HiddenInput()
            self.fields['date_exit'].widget.attrs.update({'required': True, 'class': 'form-control datepicker'})

            self.fields['hour_entry'].widget = forms.HiddenInput()
            self.fields['hour_exit'].widget.attrs.update({'required': True, 'class': 'form-control pickatime'})

    def save(self, commit=True):
        delivery_vehicle = super().save(commit=False)
        if commit:
            delivery_vehicle.save()
        return delivery_vehicle

    class Meta:
        model = ActDeliveryVehicle
        fields = "__all__"


class InventoryDeliveryVehicleForm(forms.ModelForm):
    vehicle_inventory_entry = forms.ModelMultipleChoiceField(
        queryset=VehicleInventory.objects.all(), required=False,
        widget=forms.CheckboxSelectMultiple())
    vehicle_inventory_exit = forms.ModelMultipleChoiceField(
        queryset=VehicleInventory.objects.all(), required=False,
        widget=forms.CheckboxSelectMultiple())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['vehicle_inventory_entry'].widget.attrs.update(
            {'placeholder': 'Vehicle Inventory Entry', 'class': 'styled'})
        self.fields['vehicle_inventory_exit'].widget.attrs.update(
            {'placeholder': 'Vehicle Inventory Exit', 'class': 'styled'})
        self.fields['vehicle_inventory_entry'].required = False
        self.fields['vehicle_inventory_exit'].required = False
        if self.instance.id:
            self.fields['vehicle_inventory_entry'].widget = forms.MultipleHiddenInput()

    class Meta:
        model = InventoryDeliveryVehicle
        fields = ["vehicle_inventory_entry", "vehicle_inventory_exit"]

    def save(self, delivery_vehicle=None, *args, **kwargs):
        inventory_delivery_vehicle = super().save(*args, **kwargs)
        if delivery_vehicle:
            inventory_delivery_vehicle.act_delivery_vehicle = delivery_vehicle
        inventory_delivery_vehicle.save()
        return inventory_delivery_vehicle


class ObservationDeliveryVehicleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['observation_inspection'].widget.attrs.update(
            {'placeholder': 'Observation Inspection', "rows": "5", 'class': 'form-control'})
        self.fields['observation_evaluation'].widget.attrs.update(
            {'placeholder': 'Observation Evaluation', "rows": "5", 'class': 'form-control'})
        self.fields['observation_correction'].widget.attrs.update(
            {'placeholder': 'Observation Correction', "rows": "5", 'class': 'form-control'})
        self.fields['observation_conclusion'].widget.attrs.update(
            {'placeholder': 'Observation Conclusion', "rows": "5", 'class': 'form-control'})

    class Meta:
        model = ObservationDeliveryVehicle
        fields = ["observation_inspection", "observation_evaluation",
                  "observation_correction", "observation_conclusion"]

    def save(self, delivery_vehicle=None, *args, **kwargs):
        observation_delivery_vehicle = super().save(*args, **kwargs)
        if delivery_vehicle:
            observation_delivery_vehicle.act_delivery_vehicle = delivery_vehicle
        observation_delivery_vehicle.save()
        return observation_delivery_vehicle


class WorkAssignmentForm(forms.ModelForm):
    applicant = forms.ModelChoiceField(
        queryset=User.objects.all(), empty_label=None, widget=forms.Select(
            attrs={'placeholder': 'User', 'required': True, 'class': 'form-control'}))
    frm_serie = forms.CharField(
        required=False, widget=forms.TextInput(
            attrs={"readonly": True, "disabled": True, 'class': 'form-control'}))
    frm_vin = forms.CharField(
        required=False, widget=forms.TextInput(
            attrs={"readonly": True, "disabled": True, 'class': 'form-control'}))
    frm_motor = forms.CharField(
        required=False, widget=forms.TextInput(
            attrs={"readonly": True, "disabled": True, 'class': 'form-control'}))
    frm_brand = forms.CharField(
        required=False, widget=forms.TextInput(
            attrs={"readonly": True, "disabled": True, 'class': 'form-control'}))
    frm_model = forms.CharField(
        required=False, widget=forms.TextInput(
            attrs={"readonly": True, "disabled": True, 'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        initial = kwargs.get('initial', None)
        self.fields['code_wka_maintenance'].widget.attrs.update(
            {'placeholder': 'Code WKA.', 'required': True,
             'class': 'form-control'})
        self.fields['vehicle'].widget.attrs.update(
            {'placeholder': 'Vehicle', 'required': True,
             'class': 'form-control'})
        self.fields['client'].widget.attrs.update(
            {'placeholder': 'Client', 'required': True,
             'class': 'form-control'})
        if initial:
            self.fields['code_wka_maintenance'].initial = initial["code_atm"]["current_aggregate_format"]
            self.fields['code_wka_maintenance'].widget.attrs.update({'readonly': True})
            self.fields['applicant'].queryset = User.objects.filter(pk=initial["user"].id)

        if self.instance.id:
            vehicle_detail = VehicleDetail.objects.get(vehicle=self.instance.vehicle)
            self.fields['frm_serie'].initial = vehicle_detail.number_serie
            self.fields['frm_vin'].initial = vehicle_detail.number_vin
            self.fields['frm_motor'].initial = vehicle_detail.number_motor
            self.fields['frm_brand'].initial = self.instance.vehicle.brand
            self.fields['frm_model'].initial = self.instance.vehicle.model

    class Meta:
        model = WorkAssignment
        fields = "__all__"


class WorkAssignmentDetailForm(forms.ModelForm):
    frm_description_mechanic = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Description Mechanic', 'class': 'form-control',
               "rows": "5", "disabled": True}), required=False)
    frm_is_finished_mechanic = forms.CharField(
        widget=forms.CheckboxInput(), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['labour_category'].widget.attrs.update(
            {'placeholder': 'Labour Category', 'required': True,
             'class': 'form-control cate_labour'})
        self.fields['labour'].widget.attrs.update(
            {'placeholder': 'Labour', 'required': True,
             'class': 'form-control'})
        self.fields['description_labour'].widget.attrs.update(
            {'placeholder': 'Description Labour', 'required': True,
             'class': 'form-control', "rows": "5"})
        self.fields['mechanic'].widget.attrs.update(
            {'placeholder': 'Mechanic', 'class': 'form-control'})
        self.fields['description_mechanic'].widget.attrs.update(
            {'placeholder': 'Description Mechanic', 'class': 'form-control', "rows": "5"})
        self.fields['is_finished_mechanic'].widget.attrs.update({'class': 'styled'})
        self.fields['frm_is_finished_mechanic'].widget.attrs.update({'class': 'styled', "disabled": True})
        self.fields['is_finished_supervisor'].widget.attrs.update({'class': 'styled cls_chk'})

        labour_category_id = self.data.get("labour_category", None)
        if self.instance.id:
            finished_mechanic = False
            if self.instance.is_finished_mechanic:
                finished_mechanic = True
            self.fields['labour'].queryset = Labour.objects.filter(
                labour_category=self.instance.labour_category)
            self.fields['description_mechanic'].widget = forms.HiddenInput()
            self.fields['is_finished_mechanic'].widget = forms.HiddenInput()
            self.fields['is_finished_mechanic'].widget = forms.HiddenInput()
            self.fields['frm_description_mechanic'].initial = self.instance.description_mechanic

            self.fields['frm_is_finished_mechanic'].initial = finished_mechanic
        else:
            if labour_category_id:
                self.fields['labour'].queryset = Labour.objects.filter(
                    labour_category_id=labour_category_id)

    class Meta:
        model = WorkAssignmentDetail
        fields = "__all__"


class WorkAssignmentStoreForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].widget.attrs.update(
            {'placeholder': 'Product', 'required': True,
             'class': 'form-control'})
        self.fields['quantity'].widget.attrs.update(
            {'placeholder': 'Quantity', 'required': True,
             'class': 'form-control'})

    class Meta:
        model = WorkAssignmentStore
        fields = "__all__"


class MechanicObservationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description_mechanic'].widget.attrs.update(
            {'placeholder': 'Description Mechanic',
             'class': 'form-control', "rows": "5"})
        self.fields['is_finished_mechanic'].widget.attrs.update(
            {'placeholder': 'Is Finished Mechanic', 'class': 'styled'})

    class Meta:
        model = WorkAssignmentDetail
        fields = ["description_mechanic", "is_finished_mechanic"]


class RequisitionStoreForm(forms.ModelForm):
    frm_brand = forms.CharField(
        required=False, widget=forms.TextInput(
            attrs={"readonly": True, "disabled": True, 'class': 'form-control'}))
    frm_model = forms.CharField(
        required=False, widget=forms.TextInput(
            attrs={"readonly": True, "disabled": True, 'class': 'form-control'}))
    frm_color = forms.CharField(
        required=False, widget=forms.TextInput(
            attrs={"readonly": True, "disabled": True, 'class': 'form-control'}))
    applicant = forms.ModelChoiceField(
        queryset=User.objects.all(), empty_label=None, widget=forms.Select(
            attrs={'placeholder': 'User', 'required': True, 'class': 'form-control'}))
    status_requisition = forms.ChoiceField(
        choices=core_constants.TYPE_TALLER_REQUISITION_OPTIONS,
        widget=forms.RadioSelect(), initial=core_constants.CODE_TALLER_REQUISITION_PENDING)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        initial = kwargs.get('initial', None)
        self.fields['code_spt'].widget.attrs.update({'placeholder': 'Code', 'class': 'form-control'})
        self.fields['client'].widget.attrs.update(
            {'placeholder': 'client', 'required': True, 'class': 'form-control'})
        self.fields['applicant'].widget.attrs.update(
            {'placeholder': 'applicant', 'required': True, 'class': 'form-control'})
        self.fields['status_requisition'].widget.attrs.update({'class': 'styled'})
        if initial:
            new_code = initial["code_spt_taller"]["current_aggregate_format"]
            self.fields['code_spt'].initial = new_code
            self.fields['code_spt'].widget.attrs.update({'readonly': True})
            self.fields['applicant'].queryset = User.objects.filter(pk=initial["user"].id)

    class Meta:
        model = RequisitionStore
        fields = "__all__"


class RequisitionStoreDetailForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['vehicle'].widget.attrs.update(
            {'placeholder': 'vehicle', 'required': True, 'class': 'form-control'})
        self.fields['product_category'].widget.attrs.update(
            {'required': True, 'class': 'form-control cls_category'})
        self.fields['product'].widget.attrs.update(
            {'required': True, 'class': 'form-control'})
        self.fields['quantity'].widget.attrs.update(
            {'placeholder': 'quantity', 'required': True, 'class': 'form-control'})
        self.fields['is_urgent'].widget.attrs.update(
            {'placeholder': 'is_urgent', 'class': 'styled cls_chk'})
        self.fields['observation'].widget.attrs.update(
            {'placeholder': 'observation', 'class': 'form-control', "rows": "4", "cols": "20"})

        product_category_id = self.data.get("product_category", None)
        if self.instance.id:
            self.fields['product'].queryset = Product.objects.filter(
                product_category=self.instance.product_category)
        else:
            if product_category_id:
                self.fields['product'].queryset = Product.objects.filter(
                    product_category_id=product_category_id)

    class Meta:
        model = RequisitionStoreDetail
        fields = "__all__"

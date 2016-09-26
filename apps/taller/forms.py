from django import forms
from django.forms import ClearableFileInput

from core.models import ExchangeRate
from .models import (
    Brand, Labour, TypeLabour, Vehicle, Quotation, QuotationDetail,
    Report, ReportDocument,
    TypeCheckList, TypeTransport,
    CheckList, CheckListDetail, LabourCheckList,
    PhotoCheckList, InventoryCheckList, LabourEmployeeCheckList)


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
        self.fields['type_labour'].widget.attrs.update(
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
        fields = ["type_labour", "name", "cost_price", "sale_price"]


class TypeLabourForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'Name', 'required': True,
             'class': 'form-control'})

    class Meta:
        model = TypeLabour
        fields = ['name']


class TypeTransportForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'Name', 'required': True,
             'class': 'form-control'})

    class Meta:
        model = TypeTransport
        fields = ['name']


class TypeCheckListForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['name'].widget.attrs.update(
        #     {'placeholder': 'Name', 'required': True,
        #      'class': 'form-control'})

    class Meta:
        model = TypeCheckList
        fields = '__all__'


class VehicleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type_transport'].widget.attrs.update(
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
        fields = ["type_transport", "brand", "plaque", "model",
                  "year_car", "vin", "color", "serie_motor", "soat", "expiration_soat",
                  "poliza", "expiration_poliza", "technical_review",
                  "expiration_technical_review", "opacity_test", "expiration_opacity_test",
                  "farenet_test", "expiration_farenet_test", "is_flotilla"]

    def save(self, user=None, commit=True):
        vehicle = super().save(commit=False)
        if user:
            vehicle.subsidiary = user.get_subsidiary()
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
        self.fields['sale_price'].widget.attrs.update(
            {'placeholder': 'Sale price', 'class': 'form-control'})
        self.fields['current_date'].widget.attrs.update(
            {'placeholder': 'Current date', 'class': 'form-control'})

    class Meta:
        model = Quotation
        fields = ["client", "labour", "vehicle", "current_date"]

    def save(self, data_form_quo=None, data_form_detail=None, commit=True):
        quotation = super().save(commit=False)
        quotation.exchange_rate = ExchangeRate.objects.get(id=1)
        quotation.igv_tax = data_form_quo["igv_tax"]
        quotation.sub_total = data_form_quo["sub_total"]
        quotation.total_paid = data_form_quo["total_paid"]
        quotation.save()
        for quotation_detail in data_form_detail:
            q_detail = QuotationDetail()
            q_detail.quotation = quotation
            q_detail.description = quotation_detail["description"]
            q_detail.quantity = quotation_detail["quantity"]
            q_detail.unit_price = quotation_detail["unit_price"]
            q_detail.amount_price = quotation_detail["amount_price"]
            q_detail.save()
        return quotation


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


class ReportForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['client'].widget.attrs.update(
            {'placeholder': 'client', 'class': 'form-control'})
        self.fields['vehicle'].widget.attrs.update(
            {'placeholder': 'Vehicle', 'class': 'form-control'})
        self.fields['current_date'].widget.attrs.update(
            {'placeholder': 'Current date', 'class': 'form-control'})
        self.fields['observation'].widget.attrs.update(
            {'placeholder': 'Observation', 'class': 'form-control'})

    class Meta:
        model = Report
        fields = ["client", "vehicle", "current_date", "observation"]

    def save(self, user=None, commit=True):
        report = super().save(commit=False)
        if user:
            report.subsidiary = user.get_subsidiary()
            report.save()
        return report


class CustomClearableFileInput(ClearableFileInput):
    initial_text = ''
    input_text = ''
    clear_checkbox_label = ''
    template_with_initial = (
        # '<a href="%(initial_url)s">%(initial)s</a> '
        # '%(clear_template)s<br />%(input_text)s: %(input)s'

        '<a href="%(initial_url)s">%(initial)s</a><br />%(input_text)s: %(input)s'
    )

    template_with_clear = '%(clear)s <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label>'


class ReportDocumentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['file_image'].widget.attrs.update(
            {'placeholder': 'File', 'class': 'form-control'})

    class Meta:
        model = ReportDocument
        fields = ["file_image"]
        widgets = {
            'file_image': CustomClearableFileInput(),
        }

    def save(self, report=None, commit=True):
        report_document = super().save(commit=False)
        if report:
            report_document.report = report
            report.save()
        return report_document


class CheckListForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['client'].widget.attrs.update(
            {'placeholder': 'Client', 'class': 'form-control'})
        self.fields['vehicle'].widget.attrs.update(
            {'placeholder': 'Vehicle', 'class': 'form-control'})
        self.fields['destination'].widget.attrs.update(
            {'placeholder': 'destination', 'class': 'form-control'})
        self.fields['number_billing'].widget.attrs.update(
            {'placeholder': 'Number billing', 'class': 'form-control',
             'readonly': True})
        self.fields['number_contract'].widget.attrs.update(
            {'placeholder': 'Number contract', 'class': 'form-control'})

    class Meta:
        model = CheckList
        fields = ["client", "vehicle", "destination", "number_billing", "number_contract"]

    def save(self, user=None, *args, **kwargs):
        checklist = super().save(*args, **kwargs)
        if user:
            checklist.subsidiary = user.get_subsidiary()
        checklist.save()
        return checklist


class CheckListDetailForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['service_checklist'].widget.attrs.update(
            {'placeholder': 'service ', 'class': 'form-control'})
        self.fields['type_transport'].widget.attrs.update(
            {'placeholder': 'Type Vehicle', 'class': 'form-control'})
        self.fields['type_checklist'].widget.attrs.update(
            {'placeholder': 'type checklist', 'class': 'form-control'})
        self.fields['taxi_driver'].widget.attrs.update(
            {'placeholder': 'Taxi driver', 'class': 'form-control'})
        self.fields['date_initial'].widget.attrs.update(
            {'placeholder': 'date initial', 'class': 'form-control'})
        self.fields['hour_initial'].widget.attrs.update(
            {'placeholder': 'hour initial', 'class': 'form-control'})
        self.fields['fuel_initial'].widget.attrs.update(
            {'placeholder': 'Fuel initial', 'class': 'form-control'})
        self.fields['km_initial'].widget.attrs.update(
            {'placeholder': 'km_initial', 'class': 'form-control'})
        self.fields['kms_next_maintenance'].widget.attrs.update(
            {'placeholder': 'Kms next maintenance', 'class': 'form-control'})
        self.fields['observation'].widget.attrs.update(
            {'placeholder': 'Observation', 'class': 'form-control', 'rows': "5"})

    class Meta:
        model = CheckListDetail
        fields = ["service_checklist", "type_checklist", "type_transport", "km_initial",
                  "taxi_driver", "date_initial", "hour_initial", "fuel_initial",
                  "kms_next_maintenance", "observation"]

    def save(self, checklist=None, commit=True):
        checklist_detail = super().save(commit=False)
        if checklist:
            checklist_detail.checklist = checklist
        checklist_detail.save()
        return checklist_detail


class InventoryCheckListForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['inventory_checklist'].widget.attrs.update(
            {'placeholder': 'Inventory checklist', 'class': 'form-control'})

    class Meta:
        model = InventoryCheckList
        fields = ["inventory_checklist"]

    def save(self, checklist_detail=None, commit=True):
        inventory_checklist = super().save(commit=False)
        if checklist_detail:
            inventory_checklist.checklist_detail = checklist_detail
        inventory_checklist.save()
        return inventory_checklist


class PhotoCheckListForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['photo_checklist'].widget.attrs.update(
            {'placeholder': 'photo checklist', 'class': 'form-control'})

    class Meta:
        model = PhotoCheckList
        fields = ["photo_checklist"]

    def save(self, checklist_detail=None, commit=True):
        photo_checklist = super().save(commit=False)
        if checklist_detail:
            photo_checklist.checklist_detail = checklist_detail
        photo_checklist.save()
        return photo_checklist


class LabourCheckListForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['labour'].widget.attrs.update(
            {'placeholder': 'Labour', 'class': 'form-control'})
        self.fields['employee'].widget.attrs.update(
            {'placeholder': 'Employee', 'class': 'form-control'})

    class Meta:
        model = LabourCheckList
        fields = ["labour", "employee"]

    def save(self, checklist_detail=None, commit=True):
        labour_checklist = super().save(commit=False)
        if checklist_detail:
            labour_checklist.checklist_detail = checklist_detail
        labour_checklist.save()
        return labour_checklist


class LabourEmployeeCheckListForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['task'].widget.attrs.update(
            {'placeholder': 'Task', 'class': 'form-control'})
        self.fields['is_status'].widget.attrs.update(
            {'placeholder': 'is status', 'class': 'form-control'})

    class Meta:
        model = LabourEmployeeCheckList
        fields = ["task", "is_status"]

    def save(self, labour_checklist=None, commit=True):
        labour_checklist_employee = super().save(commit=False)
        if labour_checklist:
            labour_checklist_employee.labour_checklist = labour_checklist
        labour_checklist_employee.save()
        return labour_checklist_employee

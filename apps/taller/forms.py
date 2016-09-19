from django import forms
from django.forms import ClearableFileInput

from core.models import ExchangeRate
from .constants import CODE_STATUS_AVAILABLE, CODE_STATUS_NULL
from .models import (
    Brand, Labour, TypeJob, Vehicle, Quotation, QuotationDetail,
    Report, ReportDocument,
    Order, OrderDocument, OrderDetail, OrderSupervision,
    TypeCheckList, TypeVehicle)


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


class TypeVehicleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'Name', 'required': True,
             'class': 'form-control'})

    class Meta:
        model = TypeVehicle
        fields = ['name']



class TypeCheckListForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'Name', 'required': True,
             'class': 'form-control'})

    class Meta:
        model = TypeCheckList
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
        self.fields['sale_price'].widget.attrs.update(
            {'placeholder': 'Sale price', 'class': 'form-control'})
        self.fields['current_date'].widget.attrs.update(
            {'placeholder': 'Current date', 'class': 'form-control'})
        # self.fields['exchange_rate'].widget.attrs.update(
        #     {'placeholder': 'Exchange rate', 'class': 'form-control'})
        # self.fields['igv_tax'].widget.attrs.update(
        #     {'placeholder': 'igv tax', 'class': 'form-control'})
        # self.fields['sub_total'].widget.attrs.update(
        #     {'placeholder': 'Sub total', 'class': 'form-control'})
        # self.fields['total_paid'].widget.attrs.update(
        #     {'placeholder': 'Total paid', 'class': 'form-control'})

    class Meta:
        model = Quotation
        fields = ["client", "labour", "vehicle", "current_date"]

    def save(self, data_form_quo=None, data_form_detail=None, commit=True):
        quotation = super().save(commit=False)
        quotation.exchange_rate = ExchangeRate.objects.get(pk=1)
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


class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['client'].widget.attrs.update(
            {'placeholder': 'Client', 'class': 'form-control'})
        self.fields['vehicle'].widget.attrs.update(
            {'placeholder': 'Vehicle', 'class': 'form-control'})
        self.fields['type_checklist'].widget.attrs.update(
            {'placeholder': 'Type checklist', 'class': 'form-control'})
        self.fields['number'].widget.attrs.update(
            {'placeholder': 'Number', 'class': 'form-control'})
        self.fields['date'].widget.attrs.update(
            {'placeholder': 'Date', 'class': 'form-control'})
        self.fields['taxi_driver'].widget.attrs.update(
            {'placeholder': 'Taxi driver', 'class': 'form-control'})
        self.fields['destination'].widget.attrs.update(
            {'placeholder': 'Destination', 'class': 'form-control'})
        self.fields['date_arrival'].widget.attrs.update(
            {'placeholder': 'Date arrival', 'class': 'form-control'})
        self.fields['hour_arrival'].widget.attrs.update(
            {'placeholder': 'Hour arrival', 'class': 'form-control'})
        self.fields['fuel_arrival'].widget.attrs.update(
            {'placeholder': 'Fuel arrival', 'class': 'form-control'})
        self.fields['unit_number_arrival'].widget.attrs.update(
            {'placeholder': 'Unit number arrival', 'class': 'form-control'})
        self.fields['km_arrival'].widget.attrs.update(
            {'placeholder': 'Km arrival', 'class': 'form-control'})
        self.fields['date_exit'].widget.attrs.update(
            {'placeholder': 'Date exit', 'class': 'form-control'})
        self.fields['hour_exit'].widget.attrs.update(
            {'placeholder': 'Hour exit', 'class': 'form-control'})
        self.fields['fuel_exit'].widget.attrs.update(
            {'placeholder': 'Fuel exit', 'class': 'form-control'})
        self.fields['unit_number_exit'].widget.attrs.update(
            {'placeholder': 'Unit number exit', 'class': 'form-control'})
        self.fields['km_exit'].widget.attrs.update(
            {'placeholder': 'Km exit', 'class': 'form-control'})
        self.fields['kms_next_maintenance'].widget.attrs.update(
            {'placeholder': 'Kms next maintenance', 'class': 'form-control'})
        self.fields['number_billing'].widget.attrs.update(
            {'placeholder': 'Number billing', 'class': 'form-control'})
        self.fields['number_contract'].widget.attrs.update(
            {'placeholder': 'Number contract', 'class': 'form-control'})
        self.fields['status_order'].widget.attrs.update(
            {'placeholder': 'Status order', 'class': 'form-control'})
        self.fields['type_order'].widget.attrs.update(
            {'placeholder': 'Type order', 'class': 'form-control'})
        self.fields['observation_delivery'].widget.attrs.update(
            {'placeholder': 'Observation delivery', 'class': 'form-control'})
        self.fields['observation_refund'].widget.attrs.update(
            {'placeholder': 'Observation refund', 'class': 'form-control'})
        self.fields['observation_inspection'].widget.attrs.update(
            {'placeholder': 'Observation inspection', 'class': 'form-control'})

    class Meta:
        model = Order
        fields = ["client", "vehicle", "type_checklist",
                  "number", "date", "taxi_driver", "destination",
                  "date_arrival", "hour_arrival", "fuel_arrival", "unit_number_arrival",
                  "km_arrival", "date_exit", "hour_exit", "fuel_exit",
                  "unit_number_exit", "km_exit", "kms_next_maintenance", "number_billing",
                  "number_contract", "status_order", "type_order", "observation_delivery",
                  "observation_refund", "observation_inspection"]

    def save(self, user=None, commit=True):
        order = super().save(commit=False)
        if user:
            order.subsidiary = user.get_subsidiary()
            order.save()
        return order


class OrderDocumentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['file_image'].widget.attrs.update(
            {'placeholder': 'File image', 'class': 'form-control'})

    class Meta:
        model = OrderDocument
        fields = ["file_image"]

    def save(self, order=None, commit=True):
        order_doc = super().save(commit=False)
        if order:
            order_doc.order = order
            order_doc.save()
        return order_doc


class OrderDetailForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type_vehicle'].widget.attrs.update(
            {'placeholder': 'Type vehicle', 'class': 'form-control'})
        self.fields['labour'].widget.attrs.update(
            {'placeholder': 'Labour', 'class': 'form-control'})
        self.fields['employee'].widget.attrs.update(
            {'placeholder': 'Employee', 'class': 'form-control'})
        self.fields['status_order'].widget.attrs.update(
            {'placeholder': 'Status', 'class': 'form-control'})

    class Meta:
        model = OrderDetail
        fields = ["type_vehicle", "labour", "employee", "status_order"]

    def save(self, order=None, commit=True):
        order_detail = super().save(commit=False)
        if order:
            order_detail.order = order
            order_detail.save()
        return order_detail


class OrderSupervisionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['employee'].widget.attrs.update(
            {'placeholder': 'Employee', 'class': 'form-control'})
        self.fields['observation'].widget.attrs.update(
            {'placeholder': 'Observation', 'class': 'form-control'})
        self.fields['job_rating'].widget.attrs.update(
            {'placeholder': 'Job rating', 'class': 'form-control'})

    class Meta:
        model = OrderSupervision
        fields = ["employee", "observation", "job_rating"]

    def save(self, order_detail=None, commit=True):
        order_supervision = super().save(commit=False)
        if order_detail:
            order_supervision.order_detail = order_detail
            order_supervision.save()
        return order_supervision

from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from .forms import UnitMeasurementForm, VehicleEnrollmentForm, VehicleModelForm, VehicleBrandForm, VehicleFuelForm, \
    PurchaseConditionForm, ProductModelForm, ProductBrandForm, CurrencyForm, ExchangeRateForm, VehicleInventoryForm, \
    PersonForm, StoreForm, ServiceForm
from .mixins import AuthListView, AuthCreateView, AuthUpdateView, AuthDeleteView
from .models import UnitMeasurement, VehicleEnrollment, VehicleBrand, VehicleModel, VehicleFuel, PurchaseCondition, \
    ProductBrand, ProductModel, Currency, ExchangeRate, VehicleInventory, Person, Store, Service

"""
    UnitMeasurement
"""


class UnitMeasurementList(AuthListView):
    template_name = 'dashboard/pages/admin/unitmeasurement/unitmeasurement_list.html'
    model = UnitMeasurement
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("list UnitMeasurement")
        return context


class UnitMeasurementCreation(AuthCreateView):
    template_name = 'dashboard/pages/admin/unitmeasurement/unitmeasurement_form.html'
    model = UnitMeasurement
    success_url = reverse_lazy('UnitMeasurement:list')
    form_class = UnitMeasurementForm


class UnitMeasurementUpdate(AuthUpdateView):
    template_name = 'dashboard/pages/admin/unitmeasurement/unitmeasurement_form.html'
    model = UnitMeasurement
    success_url = reverse_lazy('UnitMeasurement:list')
    form_class = UnitMeasurementForm


class UnitMeasurementDelete(AuthDeleteView):
    template_name = 'dashboard/pages/admin/unitmeasurement/unitmeasurement_confirm_delete.html'
    model = UnitMeasurement
    success_url = reverse_lazy('UnitMeasurement:list')


"""
    VehicleEnrollment
"""


class VehicleEnrollmentList(AuthListView):
    template_name = 'dashboard/pages/admin/vehicleenrollment/vehicleenrollment_list.html'
    model = VehicleEnrollment
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("list VehicleEnrollment")
        return context


class VehicleEnrollmentCreation(AuthCreateView):
    template_name = 'dashboard/pages/admin/vehicleenrollment/vehicleenrollment_form.html'
    model = VehicleEnrollment
    success_url = reverse_lazy('VehicleEnrollment:list')
    form_class = VehicleEnrollmentForm


class VehicleEnrollmentUpdate(AuthUpdateView):
    template_name = 'dashboard/pages/admin/vehicleenrollment/vehicleenrollment_form.html'
    model = VehicleEnrollment
    success_url = reverse_lazy('VehicleEnrollment:list')
    form_class = VehicleEnrollmentForm


class VehicleEnrollmentDelete(AuthDeleteView):
    template_name = 'dashboard/pages/admin/vehicleenrollment/vehicleenrollment_confirm_delete.html'
    model = VehicleEnrollmentForm
    success_url = reverse_lazy('VehicleEnrollment:list')


"""
    VehicleBrand
"""


class VehicleBrandList(AuthListView):
    template_name = 'dashboard/pages/admin/vehiclebrand/vehiclebrand_list.html'
    model = VehicleBrand
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("list VehicleBrand")
        return context


class VehicleBrandCreation(AuthCreateView):
    template_name = 'dashboard/pages/admin/vehiclebrand/vehiclebrand_form.html'
    model = VehicleBrand
    success_url = reverse_lazy('VehicleBrand:list')
    form_class = VehicleBrandForm


class VehicleBrandUpdate(AuthUpdateView):
    template_name = 'dashboard/pages/admin/vehiclebrand/vehiclebrand_form.html'
    model = VehicleBrand
    success_url = reverse_lazy('VehicleBrand:list')
    form_class = VehicleBrandForm


class VehicleBrandDelete(AuthDeleteView):
    template_name = 'dashboard/pages/admin/vehiclebrand/vehiclebrand_confirm_delete.html'
    model = VehicleBrand
    success_url = reverse_lazy('VehicleBrand:list')


"""
    VehicleModel
"""


class VehicleModelList(AuthListView):
    template_name = 'dashboard/pages/admin/vehiclemodel/vehiclemodel_list.html'
    model = VehicleModel
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("list VehicleModel")
        return context


class VehicleModelCreation(AuthCreateView):
    template_name = 'dashboard/pages/admin/vehiclemodel/vehiclemodel_form.html'
    model = VehicleModel
    success_url = reverse_lazy('VehicleModel:list')
    form_class = VehicleModelForm


class VehicleModelUpdate(AuthUpdateView):
    template_name = 'dashboard/pages/admin/vehiclemodel/vehiclemodel_form.html'
    model = VehicleModel
    success_url = reverse_lazy('VehicleModel:list')
    form_class = VehicleModelForm


class VehicleModelDelete(AuthDeleteView):
    template_name = 'dashboard/pages/admin/vehiclemodel/vehiclemodel_confirm_delete.html'
    model = VehicleModel
    success_url = reverse_lazy('VehicleModel:list')


"""
    VehicleFuel
"""


class VehicleFuelList(AuthListView):
    template_name = 'dashboard/pages/admin/vehiclefuel/vehiclefuel_list.html'
    model = VehicleFuel
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("list VehicleFuel")
        return context


class VehicleFuelCreation(AuthCreateView):
    template_name = 'dashboard/pages/admin/vehiclefuel/vehiclefuel_form.html'
    model = VehicleFuel
    success_url = reverse_lazy('VehicleFuel:list')
    form_class = VehicleFuelForm


class VehicleFuelUpdate(AuthUpdateView):
    template_name = 'dashboard/pages/admin/vehiclefuel/vehiclefuel_form.html'
    model = VehicleFuel
    success_url = reverse_lazy('VehicleFuel:list')
    form_class = VehicleFuelForm


class VehicleFuelDelete(AuthDeleteView):
    template_name = 'dashboard/pages/admin/vehiclefuel/vehiclefuel_confirm_delete.html'
    model = VehicleFuel
    success_url = reverse_lazy('VehicleFuel:list')


"""
    VehicleInventory
"""


class VehicleInventoryList(AuthListView):
    template_name = 'dashboard/pages/admin/vehicleinventory/vehicleinventory_list.html'
    model = VehicleInventory
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("list VehicleInventory")
        return context


class VehicleInventoryCreation(AuthCreateView):
    template_name = 'dashboard/pages/admin/vehicleinventory/vehicleinventory_form.html'
    model = VehicleInventory
    success_url = reverse_lazy('VehicleInventory:list')
    form_class = VehicleInventoryForm


class VehicleInventoryUpdate(AuthUpdateView):
    template_name = 'dashboard/pages/admin/vehicleinventory/vehicleinventory_form.html'
    model = VehicleInventory
    success_url = reverse_lazy('VehicleInventory:list')
    form_class = VehicleInventoryForm


class VehicleInventoryDelete(AuthDeleteView):
    template_name = 'dashboard/pages/admin/vehicleinventory/vehicleinventory_confirm_delete.html'
    model = VehicleInventory
    success_url = reverse_lazy('VehicleInventory:list')


"""
    PurchaseCondition
"""


class PurchaseConditionList(AuthListView):
    template_name = 'dashboard/pages/admin/purchasecondition/purchasecondition_list.html'
    model = PurchaseCondition
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("list PurchaseCondition")
        return context


class PurchaseConditionCreation(AuthCreateView):
    template_name = 'dashboard/pages/admin/purchasecondition/purchasecondition_form.html'
    model = PurchaseCondition
    success_url = reverse_lazy('PurchaseCondition:list')
    form_class = PurchaseConditionForm


class PurchaseConditionUpdate(AuthUpdateView):
    template_name = 'dashboard/pages/admin/purchasecondition/purchasecondition_form.html'
    model = PurchaseCondition
    success_url = reverse_lazy('PurchaseCondition:list')
    form_class = PurchaseConditionForm


class PurchaseConditionDelete(AuthDeleteView):
    template_name = 'dashboard/pages/admin/purchasecondition/purchasecondition_confirm_delete.html'
    model = PurchaseCondition
    success_url = reverse_lazy('PurchaseCondition:list')


"""
    ProductBrand
"""


class ProductBrandList(AuthListView):
    template_name = 'dashboard/pages/admin/productbrand/productbrand_list.html'
    model = ProductBrand
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("list ProductBrand")
        return context


class ProductBrandCreation(AuthCreateView):
    template_name = 'dashboard/pages/admin/productbrand/productbrand_form.html'
    model = ProductBrand
    success_url = reverse_lazy('ProductBrand:list')
    form_class = ProductBrandForm


class ProductBrandUpdate(AuthUpdateView):
    template_name = 'dashboard/pages/admin/productbrand/productbrand_form.html'
    model = ProductBrand
    success_url = reverse_lazy('ProductBrand:list')
    form_class = ProductBrandForm


class ProductBrandDelete(AuthDeleteView):
    template_name = 'dashboard/pages/admin/productbrand/productbrand_confirm_delete.html'
    model = ProductBrand
    success_url = reverse_lazy('ProductBrand:list')


"""
    ProductModel
"""


class ProductModelList(AuthListView):
    template_name = 'dashboard/pages/admin/productmodel/productmodel_list.html'
    model = ProductModel
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("list ProductModel")
        return context


class ProductModelCreation(AuthCreateView):
    template_name = 'dashboard/pages/admin/productmodel/productmodel_form.html'
    model = ProductModel
    success_url = reverse_lazy('ProductModel:list')
    form_class = ProductModelForm


class ProductModelUpdate(AuthUpdateView):
    template_name = 'dashboard/pages/admin/productmodel/productmodel_form.html'
    model = ProductModel
    success_url = reverse_lazy('ProductModel:list')
    form_class = ProductModelForm


class ProductModelDelete(AuthDeleteView):
    template_name = 'dashboard/pages/admin/productmodel/productmodel_confirm_delete.html'
    model = ProductModel
    success_url = reverse_lazy('ProductModel:list')


"""
    Currency
"""


class CurrencyList(AuthListView):
    template_name = 'dashboard/pages/admin/currency/currency_list.html'
    model = Currency
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("list Currency")
        return context


class CurrencyCreation(AuthCreateView):
    template_name = 'dashboard/pages/admin/currency/currency_form.html'
    model = Currency
    success_url = reverse_lazy('Currency:list')
    form_class = ProductModelForm


class CurrencyUpdate(AuthUpdateView):
    template_name = 'dashboard/pages/admin/currency/currency_form.html'
    model = Currency
    success_url = reverse_lazy('Currency:list')
    form_class = CurrencyForm


class CurrencyDelete(AuthDeleteView):
    template_name = 'dashboard/pages/admin/currency/currency_confirm_delete.html'
    model = Currency
    success_url = reverse_lazy('Currency:list')


"""
    Exchange Rate
"""


class ExchangeRateList(AuthListView):
    template_name = 'dashboard/pages/admin/exchangerate/exchangerate_list.html'
    model = ExchangeRate
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("list ExchangeRate")
        return context


class ExchangeRateCreation(AuthCreateView):
    template_name = 'dashboard/pages/admin/exchangerate/exchangerate_form.html'
    model = ExchangeRate
    success_url = reverse_lazy('ExchangeRate:list')
    form_class = ExchangeRateForm


class ExchangeRateUpdate(AuthUpdateView):
    template_name = 'dashboard/pages/admin/exchangerate/exchangerate_form.html'
    model = ExchangeRate
    success_url = reverse_lazy('ExchangeRate:list')
    form_class = ExchangeRateForm


class ExchangeRateDelete(AuthDeleteView):
    template_name = 'dashboard/pages/admin/exchangerate/exchangerate_confirm_delete.html'
    model = ExchangeRate
    success_url = reverse_lazy('ExchangeRate:list')


"""
    Service
"""


class ServiceList(AuthListView):
    template_name = 'dashboard/pages/admin/service/service_list.html'
    model = Service
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("list Service")
        return context


class ServiceCreation(AuthCreateView):
    template_name = 'dashboard/pages/admin/service/service_form.html'
    model = Service
    success_url = reverse_lazy('Service:list')
    form_class = ServiceForm


class ServiceUpdate(AuthUpdateView):
    template_name = 'dashboard/pages/admin/service/service_form.html'
    model = Service
    success_url = reverse_lazy('Service:list')
    form_class = ServiceForm


class ServiceDelete(AuthDeleteView):
    template_name = 'dashboard/pages/admin/service/service_confirm_delete.html'
    model = Service
    success_url = reverse_lazy('Service:list')


"""
    Store
"""


class StoreList(AuthListView):
    template_name = 'dashboard/pages/admin/store/store_list.html'
    model = Store
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("list Store")
        return context


class StoreCreation(AuthCreateView):
    template_name = 'dashboard/pages/admin/store/store_form.html'
    model = Store
    success_url = reverse_lazy('Store:list')
    form_class = StoreForm


class StoreUpdate(AuthUpdateView):
    template_name = 'dashboard/pages/admin/store/store_form.html'
    model = Store
    success_url = reverse_lazy('Store:list')
    form_class = StoreForm


class StoreDelete(AuthDeleteView):
    template_name = 'dashboard/pages/admin/store/store_confirm_delete.html'
    model = Store
    success_url = reverse_lazy('Store:list')


"""
    Person
"""


class PersonList(AuthListView):
    template_name = 'dashboard/pages/admin/person/person_list.html'
    model = Person
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("list Person")
        return context


class PersonCreation(AuthCreateView):
    template_name = 'dashboard/pages/admin/person/person_form.html'
    model = Person
    success_url = reverse_lazy('Person:list')
    form_class = PersonForm


class PersonUpdate(AuthUpdateView):
    template_name = 'dashboard/pages/admin/person/person_form.html'
    model = ExchangeRate
    success_url = reverse_lazy('Person:list')
    form_class = PersonForm


class PersonDelete(AuthDeleteView):
    template_name = 'dashboard/pages/admin/person/person_confirm_delete.html'
    model = Person
    success_url = reverse_lazy('Person:list')

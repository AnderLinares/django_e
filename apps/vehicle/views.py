# Create your views here.
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from core.mixins import AuthListView, AuthUpdateView, AuthCreateView, AuthDeleteView
from .forms import VehicleForm, VehicleDetailForm
from .formset import VehicleImageFormSet
from .models import Vehicle, VehicleDetail, VehicleImage

"""
    Vehicle
"""


class VehicleList(AuthListView):
    template_name = 'dashboard/pages/vehicle/vehicle/vehicle_list.html'
    model = Vehicle
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("list Vehicle")
        return context


class VehicleCreation(AuthCreateView):
    template_name = 'dashboard/pages/vehicle/vehicle/vehicle_form.html'
    model = Vehicle
    success_url = reverse_lazy('Vehicle:list')
    form_class = VehicleForm

    def __init__(self, **kwargs):
        self.prefix_vehicle_image = 'vehicle_image_prefix'
        super().__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)
        self.vehicle_detail_form = VehicleDetailForm()
        self.vehicle_image_formset = VehicleImageFormSet(prefix=self.prefix_vehicle_image)
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        vehicle_detail_form = VehicleDetailForm(request.POST)
        vehicle_image_formset = VehicleImageFormSet(
            request.POST, request.FILES, prefix=self.prefix_vehicle_image)
        if form.is_valid() and vehicle_detail_form.is_valid() and vehicle_image_formset.is_valid():
            return self.form_valid(form, vehicle_detail_form, vehicle_image_formset)
        else:
            return self.form_invalid(form, vehicle_detail_form, vehicle_image_formset)

    def form_valid(self, form, vehicle_detail_form, vehicle_image_formset):
        self.object = form.save(commit=False)
        self.object.save()
        vehicle_detail_form.save(vehicle=self.object, commit=False)
        vehicle_image_formset.instance = self.object
        vehicle_image_formset.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, vehicle_detail_form, vehicle_image_formset):
        self.form = form
        self.vehicle_detail_form = vehicle_detail_form
        self.vehicle_image_formset = vehicle_image_formset
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form
        context["vehicle_detail_form"] = self.vehicle_detail_form
        context["vehicle_image_formset"] = self.vehicle_image_formset
        return context


class VehicleUpdate(AuthUpdateView):
    template_name = 'dashboard/pages/vehicle/vehicle/vehicle_form.html'
    model = Vehicle
    success_url = reverse_lazy('Vehicle:list')
    form_class = VehicleForm

    def __init__(self, **kwargs):
        self.prefix_vehicle_image = 'vehicle_image_prefix'
        super().__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)
        self.object = self.get_object()
        vehicle_detail = VehicleDetail.objects.get(vehicle=self.object)
        self.vehicle_detail_form = VehicleDetailForm(instance=vehicle_detail)
        self.vehicle_image_formset = VehicleImageFormSet(instance=self.object, prefix=self.prefix_vehicle_image)
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        vehicle_detail = VehicleDetail.objects.get(vehicle=self.object)
        vehicle_detail_form = VehicleDetailForm(self.request.POST, instance=vehicle_detail)
        vehicle_image_formset = VehicleImageFormSet(
            self.request.POST, self.request.FILES, instance=self.object, prefix=self.prefix_vehicle_image)
        if form.is_valid() and vehicle_detail_form.is_valid() and vehicle_image_formset.is_valid():
            return self.form_valid(form, vehicle_detail_form, vehicle_image_formset)
        else:
            return self.form_invalid(form, vehicle_detail_form, vehicle_image_formset)

    def form_valid(self, form, vehicle_detail_form, vehicle_image_formset):
        self.object = form.save(commit=False)
        self.object.save()
        vehicle_detail_form.save(vehicle=self.object, commit=False)
        vehicle_image_formset.instance = self.object
        vehicle_image_formset.save(commit=False)
        vehicle_image_formset.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, vehicle_detail_form, vehicle_image_formset):
        self.form = form
        self.vehicle_detail_form = vehicle_detail_form
        self.vehicle_image_formset = vehicle_image_formset
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form
        context["vehicle_detail_form"] = self.vehicle_detail_form
        context["vehicle_image_formset"] = self.vehicle_image_formset
        return context


class VehicleDelete(AuthDeleteView):
    template_name = 'dashboard/pages/vehicle/vehicle/vehicle_confirm_delete.html'
    model = Vehicle
    success_url = reverse_lazy('Vehicle:list')

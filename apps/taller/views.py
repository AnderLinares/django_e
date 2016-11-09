from django.db import transaction
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from apps.company.models import Correlative
from core.mixins import AuthListView, AuthDeleteView, AuthDetailView, AuthCreateView, \
    AuthUpdateView
from .forms import ActDeliveryVehicleForm, InventoryDeliveryVehicleForm, ObservationDeliveryVehicleForm, \
    WorkAssignmentForm, MechanicObservationForm, RequisitionStoreForm
from .formset import WorkAssignmentDetailFormSet, WorkAssignmentStoreFormSet, RequisitionStoreFormSet
from .models import ActDeliveryVehicle, InventoryDeliveryVehicle, ObservationDeliveryVehicle, WorkAssignment, \
    WorkAssignmentDetail, RequisitionStore, RequisitionStoreDetail, WorkAssignmentStore


class ActDeliveryVehicleList(AuthListView):
    template_name = 'dashboard/pages/taller/delivery_vehicle/act_delivery_vehicle_list.html'
    model = ActDeliveryVehicle
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("list ActDeliveryVehicle")
        return context


class ActDeliveryVehicleCreation(AuthCreateView):
    template_name = 'dashboard/pages/taller/delivery_vehicle/act_delivery_vehicle_form.html'
    model = ActDeliveryVehicle
    success_url = reverse_lazy('ActDeliveryVehicle:list')
    form_class = ActDeliveryVehicleForm

    def get_initial(self):
        super().get_initial()
        _subsidiary = self.request.user.get_profile
        code_adv = Correlative.get_current_document('ADV', _subsidiary.subsidiary)
        self.parameter = dict(code_adv=code_adv, user=_subsidiary.user)
        return self.parameter

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)
        self.form_inventory = InventoryDeliveryVehicleForm()
        self.form_observation = ObservationDeliveryVehicleForm()
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        form_inventory = InventoryDeliveryVehicleForm(request.POST)
        form_observation = ObservationDeliveryVehicleForm(request.POST)
        if form.is_valid() and form_inventory.is_valid() and form_observation.is_valid():
            return self.frm_valid(form, form_inventory, form_observation)
        else:
            return self.frm_invalid(form, form_inventory, form_observation)

    def frm_valid(self, form, form_inventory, form_observation):
        with transaction.atomic():
            self.object = form.save(commit=True)
            form_inventory.save(delivery_vehicle=self.object, commit=False)
            form_inventory.save_m2m()
            form_observation.save(delivery_vehicle=self.object, commit=False)
            _subsidiary = self.request.user.get_profile
            Correlative.save_current_document('ADV', _subsidiary.subsidiary)
        return HttpResponseRedirect(self.get_success_url())

    def frm_invalid(self, form, form_inventory, form_observation):
        self.form = form
        self.form_inventory = form_inventory
        self.form_observation = form_observation
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form
        context["form_inventory"] = self.form_inventory
        context["form_observation"] = self.form_observation
        context["hidden_entry"] = True
        context["hidden_exit"] = False
        return context


class ActDeliveryVehicleUpdate(AuthUpdateView):
    template_name = 'dashboard/pages/taller/delivery_vehicle/act_delivery_vehicle_form.html'
    model = ActDeliveryVehicle
    success_url = reverse_lazy('ActDeliveryVehicle:list')
    form_class = ActDeliveryVehicleForm

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)
        act_inventory = InventoryDeliveryVehicle.objects.get(act_delivery_vehicle=self.object)
        obsv_inventory = ObservationDeliveryVehicle.objects.get(act_delivery_vehicle=self.object)
        self.form_inventory = InventoryDeliveryVehicleForm(instance=act_inventory)
        self.form_observation = ObservationDeliveryVehicleForm(instance=obsv_inventory)
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        act_inventory = InventoryDeliveryVehicle.objects.get(act_delivery_vehicle=self.object)
        obsv_inventory = ObservationDeliveryVehicle.objects.get(act_delivery_vehicle=self.object)
        form_inventory = InventoryDeliveryVehicleForm(request.POST, instance=act_inventory)
        form_observation = ObservationDeliveryVehicleForm(request.POST, instance=obsv_inventory)

        if form.is_valid() and form_inventory.is_valid() and form_observation.is_valid():
            return self.frm_valid(form, form_inventory, form_observation)
        else:
            return self.frm_invalid(form, form_inventory, form_observation)

    def frm_valid(self, form, form_inventory, form_observation):
        with transaction.atomic():
            self.object = form.save(commit=True)
            form_inventory.save(delivery_vehicle=self.object, commit=False)
            form_inventory.save_m2m()
            form_observation.save(delivery_vehicle=self.object, commit=False)
            _subsidiary = self.request.user.get_profile
            Correlative.save_current_document('ADV', _subsidiary.subsidiary)
        return HttpResponseRedirect(self.get_success_url())

    def frm_invalid(self, form, form_inventory, form_observation):
        self.form = form
        self.form_inventory = form_inventory
        self.form_observation = form_observation
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form
        context["form_inventory"] = self.form_inventory
        context["form_observation"] = self.form_observation
        context["hidden_entry"] = False
        context["hidden_exit"] = True
        return context


class ActDeliveryVehicleDetailView(AuthDetailView):
    template_name = 'dashboard/pages/taller/delivery_vehicle/act_delivery_vehicle_detail.html'
    model = ActDeliveryVehicle

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["inventory_list"] = InventoryDeliveryVehicle.objects.filter(act_delivery_vehicle_id=self.kwargs["pk"])
        context["observation_list"] = ObservationDeliveryVehicle.objects.filter(
            act_delivery_vehicle_id=self.kwargs["pk"])
        return context


class ActDeliveryVehicleDelete(AuthDeleteView):
    template_name = 'dashboard/pages/taller/delivery_vehicle/act_delivery_vehicle_confirm_delete.html'
    model = ActDeliveryVehicle
    success_url = reverse_lazy('ActDeliveryVehicle:list')


"""
    WorkAssignment
"""


class WorkAssignmentList(AuthListView):
    template_name = 'dashboard/pages/taller/workassignment/workassignment_list.html'
    model = WorkAssignment
    paginate_by = 10
    ordering = '-date_created'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("list WorkAssignment")
        return context


class WorkAssignmentCreation(AuthCreateView):
    template_name = 'dashboard/pages/taller/workassignment/workassignment_form.html'
    model = WorkAssignment
    success_url = reverse_lazy('WorkAssignment:list')
    form_class = WorkAssignmentForm

    def __init__(self, **kwargs):
        self.prefix_work_assignment = 'work_assignment_prefix'
        super().__init__(**kwargs)

    def get_initial(self):
        super().get_initial()
        _subsidiary = self.request.user.get_profile
        code_atm = Correlative.get_current_document('ATM', _subsidiary.subsidiary)
        return dict(code_atm=code_atm, user=_subsidiary.user)

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)
        self.work_assignment_formset = WorkAssignmentDetailFormSet(
            prefix=self.prefix_work_assignment)
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        work_assignment_formset = WorkAssignmentDetailFormSet(
            request.POST, prefix=self.prefix_work_assignment)

        if form.is_valid() and work_assignment_formset.is_valid():
            return self.frm_valid(form, work_assignment_formset)
        else:
            return self.frm_invalid(form, work_assignment_formset)

    def frm_valid(self, form, work_assignment_formset):
        with transaction.atomic():
            self.object = form.save()
            work_assignment_formset.instance = self.object
            work_assignment_formset.save()
            _subsidiary = self.request.user.get_profile
            Correlative.save_current_document('ATM', _subsidiary.subsidiary)
        return HttpResponseRedirect(self.get_success_url())

    def frm_invalid(self, form, work_assignment_formset):
        self.form = form
        self.work_assignment_formset = work_assignment_formset
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form
        context["work_assignment_formset"] = self.work_assignment_formset
        return context


class WorkAssignmentUpdate(AuthUpdateView):
    template_name = 'dashboard/pages/taller/workassignment/workassignment_form.html'
    model = WorkAssignment
    success_url = reverse_lazy('WorkAssignment:list')
    form_class = WorkAssignmentForm

    def __init__(self, **kwargs):
        self.prefix_work_assignment = 'work_assignment_prefix'
        self.btn_edit = True
        super().__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)
        self.work_assignment_formset = WorkAssignmentDetailFormSet(
            instance=self.object, prefix=self.prefix_work_assignment)
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        work_assignment_formset = WorkAssignmentDetailFormSet(
            request.POST, instance=self.object, prefix=self.prefix_work_assignment)
        print(work_assignment_formset.errors)
        print(form.errors)
        print(request.POST)
        if form.is_valid() and work_assignment_formset.is_valid():
            return self.frm_valid(form, work_assignment_formset)
        else:
            return self.frm_invalid(form, work_assignment_formset)

    def frm_valid(self, form, work_assignment_formset):
        self.object = form.save()
        work_assignment_formset.instance = self.object
        work_assignment_formset.save()
        return HttpResponseRedirect(self.get_success_url())

    def frm_invalid(self, form, work_assignment_formset):
        self.form = form
        self.work_assignment_formset = work_assignment_formset
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form
        context["work_assignment_formset"] = self.work_assignment_formset
        context["btn_edit"] = self.btn_edit
        return context


class WorkAssignmentDelete(AuthDeleteView):
    template_name = 'dashboard/pages/taller/workassignment/workassignment_confirm_delete.html'
    model = WorkAssignment
    success_url = reverse_lazy('WorkAssignment:list')


class MechanicWorkAssignmentList(AuthListView):
    template_name = 'dashboard/pages/taller/mechanic_assignment/mechanic_list.html'
    model = WorkAssignment
    success_url = reverse_lazy('MechanicAssignment:list')

    def get_queryset(self):
        super().get_queryset()
        queryset = WorkAssignmentDetail.objects.filter(
            mechanic=self.request.user
        ).order_by('-date_created', 'is_finished_mechanic')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("list MechanicAssignment")
        return context


class MechanicObservationUpdate(AuthUpdateView):
    template_name = 'dashboard/pages/taller/mechanic_assignment/mechanic_observation.html'
    model = WorkAssignmentDetail
    success_url = reverse_lazy('MechanicAssignment:list')
    form_class = MechanicObservationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_detail"] = WorkAssignmentDetail.objects.get(pk=self.kwargs["pk"])
        return context


class MechanicStoreUpdate(AuthUpdateView):
    template_name = 'dashboard/pages/taller/mechanic_assignment/mechanic_store.html'
    model = WorkAssignmentDetail
    success_url = reverse_lazy('MechanicAssignment:list')
    form_class = MechanicObservationForm

    def __init__(self, **kwargs):
        self.prefix_work_assignment_store = 'work_assignment_store_prefix'
        self.btn_edit = True
        super().__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)
        self.work_assignment_store_formset = WorkAssignmentStoreFormSet(
            instance=self.object, prefix=self.prefix_work_assignment_store)
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        work_assignment_store_formset = WorkAssignmentStoreFormSet(
            request.POST, instance=self.object, prefix=self.prefix_work_assignment_store)

        if form.is_valid() and work_assignment_store_formset.is_valid():
            return self.frm_valid(form, work_assignment_store_formset)
        else:
            return self.frm_invalid(form, work_assignment_store_formset)

    def frm_valid(self, form, work_assignment_store_formset):
        self.object = form.save()
        work_assignment_store_formset.instance = self.object
        work_assignment_store_formset.save()
        _subsidiary = self.request.user.get_profile
        Correlative.save_current_document('SPT', _subsidiary.subsidiary)
        return HttpResponseRedirect(self.get_success_url())

    def frm_invalid(self, form, work_assignment_store_formset):
        self.form = form
        self.work_assignment_store_formset = work_assignment_store_formset
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["work_assignment_store_formset"] = self.work_assignment_store_formset
        return context


class MechanicWorkAssignmentDetailView(AuthDetailView):
    template_name = 'dashboard/pages/taller/mechanic_assignment/mechanic_detail.html'
    model = WorkAssignmentDetail

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["work_assignments_tore_list"] = WorkAssignmentStore.objects.filter(
            work_assignment_id=self.kwargs["pk"])
        return context


"""
    RequisitionStore
"""


class RequisitionStoreList(AuthListView):
    template_name = 'dashboard/pages/taller/requisition_store/requisition_store_list.html'
    model = RequisitionStore
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("list RequisitionStore")
        return context


class RequisitionStoreCreation(AuthCreateView):
    template_name = 'dashboard/pages/taller/requisition_store/requisition_store_form.html'
    model = RequisitionStore
    success_url = reverse_lazy('RequisitionStore:list')
    form_class = RequisitionStoreForm

    def __init__(self, **kwargs):
        self.prefix_requisition = 'requisition_store_prefix'
        super().__init__(**kwargs)

    def get_initial(self):
        super().get_initial()
        _subsidiary = self.request.user.get_profile
        code_spt_taller = Correlative.get_current_document('SPT', _subsidiary.subsidiary)
        parameter = dict(code_spt_taller=code_spt_taller, user=_subsidiary.user)
        return parameter

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)
        self.requisition_store_formset = RequisitionStoreFormSet(
            prefix=self.prefix_requisition)
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        requisition_store_formset = RequisitionStoreFormSet(
            request.POST, prefix=self.prefix_requisition)
        if form.is_valid() and requisition_store_formset.is_valid():
            return self.frm_valid(form, requisition_store_formset)
        else:
            return self.frm_invalid(form, requisition_store_formset)

    def frm_valid(self, form, requisition_store_formset):
        self.object = form.save()
        requisition_store_formset.instance = self.object
        requisition_store_formset.save()
        return HttpResponseRedirect(self.get_success_url())

    def frm_invalid(self, form, requisition_store_formset):
        self.form = form
        self.requisition_store_formset = requisition_store_formset
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form
        context["requisition_store_formset"] = self.requisition_store_formset
        return context


class RequisitionStoreUpdate(AuthUpdateView):
    template_name = 'dashboard/pages/taller/requisition_store/requisition_store_form.html'
    model = RequisitionStore
    success_url = reverse_lazy('RequisitionStore:list')
    form_class = RequisitionStoreForm

    def __init__(self, **kwargs):
        self.prefix_requisition = 'requisition_store_prefix'
        super().__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)
        self.requisition_store_formset = RequisitionStoreFormSet(
            instance=self.object, prefix=self.prefix_requisition)
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        requisition_store_formset = RequisitionStoreFormSet(
            request.POST, instance=self.object, prefix=self.prefix_requisition)
        if form.is_valid() and requisition_store_formset.is_valid():
            return self.frm_valid(form, requisition_store_formset)
        else:
            return self.frm_invalid(form, requisition_store_formset)

    def frm_valid(self, form, requisition_store_formset):
        with transaction.atomic():
            self.object = form.save()
            requisition_store_formset.instance = self.object
            requisition_store_formset.save()
            _subsidiary = self.request.user.get_profile
            Correlative.save_current_document('SPT', _subsidiary.subsidiary)
        return HttpResponseRedirect(self.get_success_url())

    def frm_invalid(self, form, requisition_store_formset):
        self.form = form
        self.requisition_store_formset = requisition_store_formset
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form
        context["requisition_store_formset"] = self.requisition_store_formset
        return context


class RequisitionStoreDelete(AuthDeleteView):
    template_name = 'dashboard/pages/taller/requisition_store/requisition_store_confirm_delete.html'
    model = RequisitionStore
    success_url = reverse_lazy('RequisitionStore:list')


class RequisitionStoreDetailView(AuthDetailView):
    template_name = 'dashboard/pages/taller/requisition_store/requisition_store_detail.html'
    model = RequisitionStore

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["requisition_store_list"] = RequisitionStoreDetail.objects.filter(
            requisition_store_id=self.kwargs["pk"])
        return context

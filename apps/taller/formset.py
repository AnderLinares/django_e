from django.forms import inlineformset_factory

from .forms import (
    WorkAssignmentDetailForm, WorkAssignmentStoreForm,
    RequisitionStoreDetailForm)
from .models import (
    WorkAssignment, WorkAssignmentDetail, WorkAssignmentStore,
    RequisitionStore, RequisitionStoreDetail
)

WorkAssignmentDetailFormSet = inlineformset_factory(
    WorkAssignment, WorkAssignmentDetail, form=WorkAssignmentDetailForm,
    min_num=1, extra=0, can_delete=True, can_order=True
)

WorkAssignmentStoreFormSet = inlineformset_factory(
    WorkAssignmentDetail, WorkAssignmentStore, form=WorkAssignmentStoreForm,
    min_num=1, extra=0, can_delete=True, can_order=True
)

RequisitionStoreFormSet = inlineformset_factory(
    RequisitionStore, RequisitionStoreDetail, form=RequisitionStoreDetailForm,
    min_num=1, extra=0, can_delete=True, can_order=True
)

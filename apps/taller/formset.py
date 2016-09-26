from __future__ import unicode_literals

from django.forms import inlineformset_factory, modelformset_factory

from .forms import (
    ReportDocumentForm, InventoryCheckListForm, PhotoCheckListForm,
    LabourCheckListForm,
    LabourEmployeeCheckListForm)
from .models import (
    Report, ReportDocument,
    CheckListDetail, InventoryCheckList, PhotoCheckList, LabourCheckList,
    LabourEmployeeCheckList)

# report
ReportDocumentFormSet = inlineformset_factory(
    Report, ReportDocument, form=ReportDocumentForm,
    min_num=1, extra=0, can_delete=True, can_order=True
)

# inventory CheckList
CheckListInventoryFormSet = inlineformset_factory(
    CheckListDetail, InventoryCheckList, form=InventoryCheckListForm,
    min_num=1, extra=0, can_delete=True, can_order=True
)

# photo CheckList
CheckListPhotoFormSet = inlineformset_factory(
    CheckListDetail, PhotoCheckList, form=PhotoCheckListForm,
    min_num=1, extra=0, can_delete=True, can_order=True
)

# labour CheckList
CheckListLabourFormSet = inlineformset_factory(
    CheckListDetail, LabourCheckList, form=LabourCheckListForm,
    min_num=1, extra=0, can_delete=True, can_order=True
)


# labour employee CheckList
CheckListLabourEmployeeFormSet = inlineformset_factory(
    LabourCheckList, LabourEmployeeCheckList, form=LabourEmployeeCheckListForm,
    min_num=1, extra=0, can_delete=True, can_order=True
)


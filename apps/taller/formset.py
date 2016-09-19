from __future__ import unicode_literals

from django.forms import inlineformset_factory

from .forms import (
    ReportDocumentForm,
    OrderDetailForm, OrderDocumentForm, OrderSupervisionForm
)
from .models import (
    Report, ReportDocument,
    Order, OrderDetail, OrderDocument, OrderSupervision
)

# report
ReportDocumentFormSet = inlineformset_factory(
    Report, ReportDocument, form=ReportDocumentForm,
    min_num=1, extra=0,  can_delete=True, can_order=True
)

# order
OrderDocumentFormSet = inlineformset_factory(
    Order, OrderDocument, form=OrderDocumentForm,
    min_num=1, extra=0,  can_delete=True, can_order=True
)

OrderDetailFormSet = inlineformset_factory(
    Order, OrderDetail, form=OrderDetailForm,
    min_num=1, extra=0,  can_delete=True, can_order=True
)

# order detail
OrderSupervisionFormSet = inlineformset_factory(
    OrderDetail, OrderSupervision, form=OrderSupervisionForm,
    min_num=1, extra=0,  can_delete=True, can_order=True
)



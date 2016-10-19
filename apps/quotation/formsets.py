from django.forms import inlineformset_factory

from .forms import QuotationStoreDetailForm
from .models import (
    QuotationStore, QuotationStoreDetail
)

QuotationStoreDetailFormSet = inlineformset_factory(
    QuotationStore, QuotationStoreDetail, form=QuotationStoreDetailForm,
    min_num=1, extra=0, can_delete=True, can_order=True)

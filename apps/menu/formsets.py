

from django.forms import inlineformset_factory

from .forms import TeamMenuItemForm
from .models import (
    TeamMenu, TeamMenuItem)

TeamMenuItemFormSet = inlineformset_factory(
    TeamMenu, TeamMenuItem, form=TeamMenuItemForm,
    min_num=1, extra=0,  can_delete=True, can_order=True)
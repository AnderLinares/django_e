from __future__ import unicode_literals

from django.forms import inlineformset_factory

from .forms import VehicleImageForm
from .models import Vehicle, VehicleImage


VehicleImageFormSet = inlineformset_factory(
    Vehicle, VehicleImage, form=VehicleImageForm,
    extra=1, can_delete=True, can_order=True)

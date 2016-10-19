from django.contrib import admin

# Register your models here.
from .models import (
    Organization, Subsidiary, Correlative,
)

admin.site.register(Organization)
admin.site.register(Subsidiary)
admin.site.register(Correlative)
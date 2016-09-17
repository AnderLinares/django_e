from django.contrib import admin

# Register your models here.

from .models import (
    Employee, BloodRecord, BloodRelative, Eps, PoliceRecord,
    ExperienceRecord, TrainingRecord
)

admin.site.register(Employee)
admin.site.register(ExperienceRecord)
admin.site.register(BloodRecord)
admin.site.register(BloodRelative)
admin.site.register(PoliceRecord)
admin.site.register(TrainingRecord)
admin.site.register(Eps)
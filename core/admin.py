from django.contrib import admin

from .models import (
    Organization, Zone, Country, State, Module, Team,
    Currency, ExchangeRate, Subsidiary, Bank, Specialty,
    ContributionSystem, TypeContributionSystem,
)

admin.site.register(Module)
admin.site.register(Team)
admin.site.register(Organization)
admin.site.register(Zone)
admin.site.register(Country)
admin.site.register(State)

admin.site.register(Currency)
admin.site.register(ExchangeRate)
admin.site.register(Subsidiary)

admin.site.register(Bank)
admin.site.register(Specialty)
admin.site.register(ContributionSystem)
admin.site.register(TypeContributionSystem)

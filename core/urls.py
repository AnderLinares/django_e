
from django.conf.urls import url, include
from .views import (
    OrganizationView, OrganizationCreateView, OrganizationEditView, OrganizationListView,
    SubsidiaryView, SubsidiaryCreateView, SubsidiaryEditView, SubsidiaryListView,
    CurrencyView, CurrencyCreateView, CurrencyEditView, CurrencyListView,
    ExchangeRateView, ExchangeRateCreateView, ExchangeRateEditView, ExchangeRateListView,
    UnitMeasurementView, UnitMeasurementCreateView, UnitMeasurementEditView, UnitMeasurementListView,
)

currency_patterns = ([
   url(r'^$', CurrencyView.as_view(), name="index"),
   url(r'^add/', CurrencyCreateView.as_view(), name="add"),
   url(r'^edit/', CurrencyEditView.as_view(), name="edit"),
   url(r'^list/', CurrencyListView.as_view(), name="list"),
], 'admin-currency')

exchangerate_patterns = ([
   url(r'^$', ExchangeRateView.as_view(), name="index"),
   url(r'^add/', ExchangeRateCreateView.as_view(), name="add"),
   url(r'^edit/', ExchangeRateEditView.as_view(), name="edit"),
   url(r'^list/', ExchangeRateListView.as_view(), name="list"),
], 'admin-exchangerate')

organization_patterns = ([
   url(r'^$', OrganizationView.as_view(), name="index"),
   url(r'^add/', OrganizationCreateView.as_view(), name="add"),
   url(r'^edit/', OrganizationEditView.as_view(), name="edit"),
   url(r'^list/', OrganizationListView.as_view(), name="list"),
], 'admin-organization')

subsidiary_patterns = ([
   url(r'^$', SubsidiaryView.as_view(), name="index"),
   url(r'^add/', SubsidiaryCreateView.as_view(), name="add"),
   url(r'^edit/', SubsidiaryEditView.as_view(), name="edit"),
   url(r'^list/', SubsidiaryListView.as_view(), name="list"),
], 'admin-subsidiary')


measurement_patterns = ([
   url(r'^$', UnitMeasurementView.as_view(), name="index"),
   url(r'^add/', UnitMeasurementCreateView.as_view(), name="add"),
   url(r'^edit/', UnitMeasurementEditView.as_view(), name="edit"),
   url(r'^list/', UnitMeasurementListView.as_view(), name="list"),
], 'admin-measurement')


urlpatterns = [
    url(r'^organization', include(organization_patterns)),
    url(r'^subsidiary/', include(subsidiary_patterns)),
    url(r'^currency/', include(currency_patterns)),
    url(r'^exchange-rate/', include(exchangerate_patterns)),
    url(r'^unit-measurement/', include(measurement_patterns)),

]

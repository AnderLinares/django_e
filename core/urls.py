from django.conf.urls import url, include
from . import views

urlpatterns = [

    url(r'^hand-work-category/',
        include([
            url(r'^$', views.HandWorkCategoryList.as_view(), name='list'),
            url(r'^new/$', views.HandWorkCategoryCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.HandWorkCategoryUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.HandWorkCategoryDelete.as_view(), name='delete'),
        ], namespace='HandWorkCategory')),
    url(r'^hand-work/',
        include([
            url(r'^$', views.HandWorkList.as_view(), name='list'),
            url(r'^new/$', views.HandWorkCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.HandWorkUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.HandWorkDelete.as_view(), name='delete'),
        ], namespace='HandWork')),

    url(r'^labour-category/',
        include([
            url(r'^$', views.LabourCategoryList.as_view(), name='list'),
            url(r'^new/$', views.LabourCategoryCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.LabourCategoryUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.LabourCategoryDelete.as_view(), name='delete'),
        ], namespace='LabourCategory')),
    url(r'^labour/',
        include([
            url(r'^$', views.LabourList.as_view(), name='list'),
            url(r'^new/$', views.LabourCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.LabourUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.LabourDelete.as_view(), name='delete'),
        ], namespace='Labour')),

    url(r'^unit-measurement/',
        include([
            url(r'^$', views.UnitMeasurementList.as_view(), name='list'),
            url(r'^new/$', views.UnitMeasurementCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.UnitMeasurementUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.UnitMeasurementDelete.as_view(), name='delete'),
        ], namespace='UnitMeasurement')),
    url(r'^vehicle-enrollment/',
        include([
            url(r'^$', views.VehicleEnrollmentList.as_view(), name='list'),
            url(r'^new/$', views.VehicleEnrollmentCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.VehicleEnrollmentUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.VehicleEnrollmentDelete.as_view(), name='delete'),
        ], namespace='VehicleEnrollment')),

    url(r'^vehicle-brand/',
        include([
            url(r'^$', views.VehicleBrandList.as_view(), name='list'),
            url(r'^new/$', views.VehicleBrandCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.VehicleBrandUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.VehicleBrandDelete.as_view(), name='delete'),
        ], namespace='VehicleBrand')),

    url(r'^vehicle-model/',
        include([
            url(r'^$', views.VehicleModelList.as_view(), name='list'),
            url(r'^new/$', views.VehicleModelCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.VehicleModelUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.VehicleModelDelete.as_view(), name='delete'),
        ], namespace='VehicleModel')),

    url(r'^vehicle-fuel/',
        include([
            url(r'^$', views.VehicleFuelList.as_view(), name='list'),
            url(r'^new/$', views.VehicleFuelCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.VehicleFuelUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.VehicleFuelDelete.as_view(), name='delete'),
        ], namespace='VehicleFuel')),

    url(r'^vehicle-inventory/',
        include([
            url(r'^$', views.VehicleInventoryList.as_view(), name='list'),
            url(r'^new/$', views.VehicleInventoryCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.VehicleInventoryUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.VehicleInventoryDelete.as_view(), name='delete'),
        ], namespace='VehicleInventory')),

    url(r'^purchase-condition/',
        include([
            url(r'^$', views.PurchaseConditionList.as_view(), name='list'),
            url(r'^new/$', views.PurchaseConditionCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.PurchaseConditionUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.PurchaseConditionDelete.as_view(), name='delete'),
        ], namespace='PurchaseCondition')),

    url(r'^product-brand/',
        include([
            url(r'^$', views.ProductBrandList.as_view(), name='list'),
            url(r'^new/$', views.ProductBrandCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.ProductBrandUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.ProductBrandDelete.as_view(), name='delete'),
        ], namespace='ProductBrand')),

    url(r'^product-model/',
        include([
            url(r'^$', views.ProductModelList.as_view(), name='list'),
            url(r'^new/$', views.ProductModelCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.ProductModelUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.ProductModelDelete.as_view(), name='delete'),
        ], namespace='ProductModel')),

    url(r'^currency/',
        include([
            url(r'^$', views.CurrencyList.as_view(), name='list'),
            url(r'^new/$', views.CurrencyCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.CurrencyUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.CurrencyDelete.as_view(), name='delete'),
        ], namespace='Currency')),

    url(r'^exchange-rate/',
        include([
            url(r'^$', views.ExchangeRateList.as_view(), name='list'),
            url(r'^new/$', views.ExchangeRateCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.ExchangeRateUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.ExchangeRateDelete.as_view(), name='delete'),
        ], namespace='ExchangeRate')),

    url(r'^service/',
        include([
            url(r'^$', views.ServiceList.as_view(), name='list'),
            url(r'^new/$', views.ServiceCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.ServiceUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.ServiceDelete.as_view(), name='delete'),
        ], namespace='Service')),

    url(r'^store/',
        include([
            url(r'^$', views.StoreList.as_view(), name='list'),
            url(r'^new/$', views.StoreCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.StoreUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.StoreDelete.as_view(), name='delete'),
        ], namespace='Store')),

    url(r'^person/',
        include([
            url(r'^$', views.PersonList.as_view(), name='list'),
            url(r'^new/$', views.PersonCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.PersonUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.PersonDelete.as_view(), name='delete'),
        ], namespace='Person')),

    url(r'^consult-service/',
        include([
            url(r'^$', views.ConsultServiceList.as_view(), name='list'),
            url(r'^new/$', views.ConsultServiceCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.ConsultServiceUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.ConsultServiceDelete.as_view(), name='delete'),
        ], namespace='ConsultService')),

    ]

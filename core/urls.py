from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^UnitMeasurement/',
        include([
            url(r'^$', views.UnitMeasurementList.as_view(), name='list'),
            url(r'^new/$', views.UnitMeasurementCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.UnitMeasurementUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.UnitMeasurementDelete.as_view(), name='delete'),
        ], namespace='UnitMeasurement')),
    url(r'^VehicleEnrollment/',
        include([
            url(r'^$', views.VehicleEnrollmentList.as_view(), name='list'),
            url(r'^new/$', views.VehicleEnrollmentCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.VehicleEnrollmentUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.VehicleEnrollmentDelete.as_view(), name='delete'),
        ], namespace='VehicleEnrollment')),

    url(r'^VehicleBrand/',
        include([
            url(r'^$', views.VehicleBrandList.as_view(), name='list'),
            url(r'^new/$', views.VehicleBrandCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.VehicleBrandUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.VehicleBrandDelete.as_view(), name='delete'),
        ], namespace='VehicleBrand')),

    url(r'^VehicleModel/',
        include([
            url(r'^$', views.VehicleModelList.as_view(), name='list'),
            url(r'^new/$', views.VehicleModelCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.VehicleModelUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.VehicleModelDelete.as_view(), name='delete'),
        ], namespace='VehicleModel')),

    url(r'^VehicleFuel/',
        include([
            url(r'^$', views.VehicleFuelList.as_view(), name='list'),
            url(r'^new/$', views.VehicleFuelCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.VehicleFuelUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.VehicleFuelDelete.as_view(), name='delete'),
        ], namespace='VehicleFuel')),

    url(r'^VehicleInventory/',
        include([
            url(r'^$', views.VehicleInventoryList.as_view(), name='list'),
            url(r'^new/$', views.VehicleInventoryCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.VehicleInventoryUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.VehicleInventoryDelete.as_view(), name='delete'),
        ], namespace='VehicleInventory')),

    url(r'^PurchaseCondition/',
        include([
            url(r'^$', views.PurchaseConditionList.as_view(), name='list'),
            url(r'^new/$', views.PurchaseConditionCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.PurchaseConditionUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.PurchaseConditionDelete.as_view(), name='delete'),
        ], namespace='PurchaseCondition')),

    url(r'^ProductBrand/',
        include([
            url(r'^$', views.ProductBrandList.as_view(), name='list'),
            url(r'^new/$', views.ProductBrandCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.ProductBrandUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.ProductBrandDelete.as_view(), name='delete'),
        ], namespace='ProductBrand')),

    url(r'^ProductModel/',
        include([
            url(r'^$', views.ProductModelList.as_view(), name='list'),
            url(r'^new/$', views.ProductModelCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.ProductModelUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.ProductModelDelete.as_view(), name='delete'),
        ], namespace='ProductModel')),

    url(r'^Currency/',
        include([
            url(r'^$', views.CurrencyList.as_view(), name='list'),
            url(r'^new/$', views.CurrencyCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.CurrencyUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.CurrencyDelete.as_view(), name='delete'),
        ], namespace='Currency')),

    url(r'^ExchangeRate/',
        include([
            url(r'^$', views.ExchangeRateList.as_view(), name='list'),
            url(r'^new/$', views.ExchangeRateCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.ExchangeRateUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.ExchangeRateDelete.as_view(), name='delete'),
        ], namespace='ExchangeRate')),

    url(r'^Service/',
        include([
            url(r'^$', views.ServiceList.as_view(), name='list'),
            url(r'^new/$', views.ServiceCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.ServiceUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.ServiceDelete.as_view(), name='delete'),
        ], namespace='Service')),

    url(r'^Store/',
        include([
            url(r'^$', views.StoreList.as_view(), name='list'),
            url(r'^new/$', views.StoreCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.StoreUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.StoreDelete.as_view(), name='delete'),
        ], namespace='Store')),

    url(r'^Person/',
        include([
            url(r'^$', views.PersonList.as_view(), name='list'),
            url(r'^new/$', views.PersonCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.PersonUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.PersonDelete.as_view(), name='delete'),
        ], namespace='Person')),


    ]

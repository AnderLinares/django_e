from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'',
        include([
            url(r'^currency/$', views.CurrencyAPIListView.as_view(), name='currency'),
            url(r'^currency/(?P<pk>[0-9]+)/$', views.CurrencyAPIView.as_view(), name='currency-detail'),
        ], namespace='api-category')),

    url(r'',
        include([
            url(r'^exchange-rate/$', views.ExchangeRateAPIListView.as_view(), name='exchangerate'),
            url(r'^exchange-rate/(?P<pk>[0-9]+)/$', views.ExchangeRateAPIView.as_view(), name='exchangerate-detail'),
        ], namespace='api-product')),

    url(r'',
        include([
            url(r'^product-brand/$', views.ProductBrandAPIListView.as_view(), name='product-brand'),
            url(r'^product-brand/(?P<pk>[0-9]+)/$', views.ProductBrandAPIView.as_view(), name='product-brand-detail'),
        ], namespace='api-product-brand')),

    url(r'',
        include([
            url(r'^product-model/$', views.ProductModelAPIListView.as_view(), name='product-model'),
            url(r'^product-model/(?P<pk>[0-9]+)/$', views.ProductModelAPIView.as_view(), name='product-model-detail'),
            url(r'^product-model/(?P<brand>[0-9]+)/brand/$', views.ProductModelBrandAPIListView.as_view(), name='product-model-brand'),
        ], namespace='api-product-model')),

    url(r'',
        include([
            url(r'^vehicle-brand/$', views.VehicleBrandAPIListView.as_view(), name='vehicle-brand'),
            url(r'^vehicle-brand/(?P<pk>[0-9]+)/$', views.VehicleBrandAPIView.as_view(), name='vehicle-brand-detail'),
        ], namespace='api-vehicle-brand')),

    url(r'',
        include([
            url(r'^vehicle-model/$', views.VehicleModelAPIListView.as_view(), name='vehicle-model'),
            url(r'^vehicle-model/(?P<pk>[0-9]+)/$', views.VehicleModelAPIView.as_view(), name='vehicle-model-detail'),
            url(r'^vehicle-model/(?P<brand>[0-9]+)/brand/$', views.VehicleModelBrandAPIListView.as_view(), name='vehicle-model-brand'),
        ], namespace='api-vehicle-model')),


]

urlpatterns = format_suffix_patterns(urlpatterns)

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
            url(r'^vehicle-model/$', views.VehicleModelAPIListView.as_view(), name='vehicle-model'),
            url(r'^vehicle-model/(?P<pk>[0-9]+)/$', views.VehicleModelAPIView.as_view(), name='vehicle-model-detail'),
            url(r'^vehicle-model/(?P<brand>[0-9]+)/brand/$', views.VehicleModelBrandAPIListView.as_view(),
                name='vehicle-model-brand'),
        ], namespace='api-vehicle-model')),

    url(r'',
        include([
            url(r'^vehicle-model/$', views.VehicleModelAPIListView.as_view(), name='vehicle-model'),
            url(r'^vehicle-model/(?P<pk>[0-9]+)/$', views.VehicleModelAPIView.as_view(), name='vehicle-model-detail'),
            url(r'^vehicle-model/(?P<brand>[0-9]+)/brand/$', views.VehicleModelBrandAPIListView.as_view(), name='vehicle-model-brand'),
        ], namespace='api-vehicle-model')),

    url(r'',
        include([
            url(r'^vehicle-enrollment/$', views.VehicleEnrollmentAPIListView.as_view(), name='vehicle-enrollment'),
            url(r'^vehicle-enrollment/(?P<pk>[0-9]+)/$', views.VehicleEnrollmentAPIView.as_view(), name='vehicle-enrollment-detail'),
        ], namespace='api-vehicle-enrollment')),

    url(r'',
        include([
            url(r'^labour-category/$', views.LabourCategoryAPIListView.as_view(), name='labour-category'),
            url(r'^labour/(?P<pk>[0-9]+)/$', views.LabourCategoryAPIView.as_view(), name='labour-category-detail'),
        ], namespace='api-labour-category')),

    url(r'',
        include([
            url(r'^labour/$', views.LabourAPIListView.as_view(), name='labour'),
            url(r'^labour/(?P<pk>[0-9]+)/$', views.LabourAPIView.as_view(), name='labour-detail'),
            url(r'^labour/(?P<labour_category>[0-9]+)/labour/$', views.LabourCategoryLabourAPIView.as_view(), name='labour-category-labour-detail'),
        ], namespace='api-labour')),


    url(r'',
        include([
            url(r'^handwork-category/$', views.HandWorkCategoryAPIListView.as_view(), name='handwork-category'),
            url(r'^handwork-category/(?P<pk>[0-9]+)/$', views.HandWorkCategoryAPIView.as_view(), name='handwork-category-detail'),
        ], namespace='api-handwork-category')),

    url(r'',
        include([
            url(r'^handwork/$', views.HandWorkAPIListView.as_view(), name='Handwork'),
            url(r'^handwork/(?P<pk>[0-9]+)/$', views.HandWorkAPIView.as_view(), name='Handwork-detail'),
            url(r'^handwork/(?P<handworkcategory>[0-9]+)/category/$', views.HandWorkCategoryHandWorkAPIView.as_view(), name='Handwork-category-Handwork-detail'),
        ], namespace='api-handwork')),

]

urlpatterns = format_suffix_patterns(urlpatterns)

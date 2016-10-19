from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'',
        include([
            url(r'^supplier/$', views.SupplierAPIListView.as_view(), name='supplier'),
            url(r'^supplier/(?P<pk>[0-9]+)/$', views.SupplierAPIView.as_view(), name='supplier-detail'),
        ], namespace='api-zone')),

    url(r'',
        include([
            url(r'^supplier-subsidiary/$', views.SupplierSubsidiaryAPIListView.as_view(), name='supplier-subsidiary'),
            url(r'^supplier-subsidiary/(?P<pk>[0-9]+)/$', views.SupplierSubsidiaryAPIView.as_view(),
                name='supplier-subsidiary-detail'),
        ], namespace='api-supplier-subsidiary')),

    url(r'',
        include([
            url(r'^supplier-product/$',
                views.SupplierProductAPIListView.as_view(), name='supplier-product'),
            url(r'^supplier-product/(?P<pk>[0-9]+)/$',
                views.SupplierProductAPIView.as_view(), name='supplier-product-detail'),
            url(r'^supplier-product/(?P<supplier>[0-9]+)/supplier/$',
                views.SupplierProductSupplierAPIListView.as_view(), name='supplier-product-supplier'),
        ], namespace='api-supplier-product')),

]

urlpatterns = format_suffix_patterns(urlpatterns)

from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^supplier/',
        include([
            url(r'^$', views.SupplierList.as_view(), name='list'),
            url(r'^new/$', views.SupplierCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.SupplierUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.SupplierDelete.as_view(), name='delete'),
        ], namespace='Supplier')),

    url(r'^supplier-subsidiary/',
        include([
            url(r'^$', views.SupplierSubsidiaryList.as_view(), name='list'),
            url(r'^new/$', views.SupplierSubsidiaryCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.SupplierSubsidiaryUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.SupplierSubsidiaryDelete.as_view(), name='delete'),
        ], namespace='SupplierSubsidiary')),

    url(r'^supplier-product/',
        include([
            url(r'^$', views.SupplierProductList.as_view(), name='list'),
            url(r'^new/$', views.SupplierProductCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.SupplierProductUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.SupplierProductDelete.as_view(), name='delete'),
        ], namespace='SupplierProduct'))
]

from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^quotation_store/',
        include([
            url(r'^$', views.QuotationStoreList.as_view(), name='list'),
            url(r'^(?P<pk>[0-9]+)/$',  views.QuotationStoreDetailView.as_view(), name='detail'),
            url(r'^new/$', views.QuotationStoreCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/delete/$', views.QuotationStoreDelete.as_view(), name='delete'),
        ], namespace='QuotationStore')),

    url(r'^quotation_maintenance/',
        include([
            url(r'^$', views.QuotationMaintenanceList.as_view(), name='list'),
            url(r'^(?P<pk>[0-9]+)/$', views.QuotationMaintenanceDetailView.as_view(), name='detail'),
            url(r'^new/$', views.QuotationMaintenanceCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/delete/$', views.QuotationMaintenanceDelete.as_view(), name='delete'),
        ], namespace='QuotationMaintenance')),

    ]

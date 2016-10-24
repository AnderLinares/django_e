from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^purchase-order/',
        include([
            url(r'^$', views.PurchaseOrderList.as_view(), name='list'),
            url(r'^(?P<pk>[0-9]+)/$',  views.PurchaseOrderDetailView.as_view(), name='detail'),
            url(r'^new/$', views.PurchaseOrderCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/delete/$', views.PurchaseOrderDelete.as_view(), name='delete'),
        ], namespace='PurchaseOrder')),

    ]

from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^act-delivery-vehicle/',
        include([
            url(r'^$', views.ActDeliveryVehicleList.as_view(), name='list'),
            url(r'^(?P<pk>[0-9]+)/$',  views.ActDeliveryVehicleDetailView.as_view(), name='detail'),
            url(r'^(?P<pk>\d+)/update/$', views.ActDeliveryVehicleUpdate.as_view(), name='update'),
            url(r'^new/$', views.ActDeliveryVehicleCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/delete/$', views.ActDeliveryVehicleDelete.as_view(), name='delete'),
        ], namespace='ActDeliveryVehicle')),

    url(r'^work-assignment/',
        include([
            url(r'^$', views.WorkAssignmentList.as_view(), name='list'),
            url(r'^(?P<pk>\d+)/update/$', views.WorkAssignmentUpdate.as_view(), name='update'),
            url(r'^new/$', views.WorkAssignmentCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/delete/$', views.WorkAssignmentDelete.as_view(), name='delete'),
        ], namespace='WorkAssignment')),

    url(r'^mechanic-assignment/',
        include([
            url(r'^$', views.MechanicWorkAssignmentList.as_view(), name='list'),
            url(r'^(?P<pk>[0-9]+)/$',  views.MechanicWorkAssignmentDetailView.as_view(), name='detail'),
            url(r'^(?P<pk>\d+)/observation-update/$', views.MechanicObservationUpdate.as_view(), name='observation-update'),
            url(r'^(?P<pk>\d+)/store-update/$', views.MechanicStoreUpdate.as_view(), name='store-update'),
        ], namespace='MechanicAssignment')),

    url(r'^requisition-store/',
        include([
            url(r'^$', views.RequisitionStoreList.as_view(), name='list'),
            url(r'^(?P<pk>[0-9]+)/$',  views.RequisitionStoreDetailView.as_view(), name='detail'),
            url(r'^(?P<pk>\d+)/update/$', views.RequisitionStoreUpdate.as_view(), name='update'),
            url(r'^new/$', views.RequisitionStoreCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/delete/$', views.RequisitionStoreDelete.as_view(), name='delete'),
        ], namespace='RequisitionStore')),

    ]

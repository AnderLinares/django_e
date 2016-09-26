from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    LabourAPIView, LabourAPIListView,
    TypeCheckListAPIView, TypeCheckListAPIListView, TypeCheckListServiceAPIListView,
    TypeTransportAPIView, TypeTransportAPIListView,
    ServiceCheckListAPIView, ServiceCheckListAPIListView
)

urlpatterns = [
    url(r'^labour/$', LabourAPIListView.as_view(), name='api-labour'),
    url(r'^labour/(?P<pk>[0-9]+)/$', LabourAPIView.as_view(), name='api-labour_detail'),

    url(r'^type_check_list/$', TypeCheckListAPIListView.as_view(), name='api-typechecklist'),
    url(r'^type_check_list/(?P<pk>[0-9]+)/$', TypeCheckListAPIView.as_view(), name='api-typechecklist_detail'),

    url(r'^type_transport/$', TypeTransportAPIListView.as_view(), name='api-typevehicle'),
    url(r'^type_transport/(?P<pk>[0-9]+)/$', TypeTransportAPIView.as_view(), name='api-typevehicle_detail'),

    url(r'^service_check_list/$', ServiceCheckListAPIListView.as_view(), name='api-service-checklist'),
    url(r'^service_check_list/(?P<pk>[0-9]+)/$', ServiceCheckListAPIView.as_view(), name='api-service-checklist_detail'),

    url(r'^service_solicitude_check_list/(?P<service>[0-9]+)/(?P<typetransport>[0-9]+)/$',
        TypeCheckListServiceAPIListView.as_view(), name='api-typechecklistservice_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

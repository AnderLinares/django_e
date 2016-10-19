from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    url(r'',
        include([
            url(r'^organization/$', views.OrganizationAPIListView.as_view(), name='organization'),
            url(r'^organization/(?P<pk>[0-9]+)/$', views.OrganizationAPIView.as_view(), name='organization-detail'),
        ], namespace='api-organization')),

    url(r'',
        include([
            url(r'^subsidiary/$', views.SubsidiaryAPIListView.as_view(), name='Subsidiary'),
            url(r'^subsidiary/(?P<pk>[0-9]+)/$', views.SubsidiaryAPIView.as_view(), name='subsidiary-detail'),
            url(r'^subsidiary/(?P<organization>[0-9]+)/organization/$', views.SubsidiaryOrganizationAPIListView.as_view(), name='subsidiary-organization'),

        ], namespace='api-Subsidiary')),

    url(r'',
        include([
            url(r'^correlative/$', views.CorrelativeAPIListView.as_view(), name='correlative'),
            url(r'^correlative/(?P<pk>[0-9]+)/$', views.CorrelativeAPIView.as_view(), name='correlative-detail'),
        ], namespace='api-correlative')),

]

urlpatterns = format_suffix_patterns(urlpatterns)

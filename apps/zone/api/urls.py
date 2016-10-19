from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    url(r'',
        include([
            url(r'^zone/$', views.ZoneAPIListView.as_view(), name='zone'),
            url(r'^zone/(?P<pk>[0-9]+)/$', views.ZoneAPIView.as_view(), name='zone-detail'),
        ], namespace='api-zone')),

    url(r'',
        include([
            url(r'^country/$', views.CountryAPIListView.as_view(), name='country'),
            url(r'^country/(?P<pk>[0-9]+)/$', views.CountryAPIView.as_view(), name='country-detail'),
            url(r'^country/(?P<zone>[0-9]+)/zone/$', views.CountryZoneAPIListView.as_view(), name='country-zone'),

        ], namespace='api-country')),

    url(r'',
        include([
            url(r'^state/$', views.StateAPIListView.as_view(), name='state'),
            url(r'^state/(?P<pk>[0-9]+)/$', views.StateAPIView.as_view(), name='state-detail'),
        ], namespace='api-state')),

]

urlpatterns = format_suffix_patterns(urlpatterns)

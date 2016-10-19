from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^zone/',
        include([
            url(r'^$', views.ZoneList.as_view(), name='list'),
            url(r'^new/$', views.ZoneCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.ZoneUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.ZoneDelete.as_view(), name='delete'),
        ], namespace='Zone')),

    url(r'^country/',
        include([
            url(r'^$', views.CountryList.as_view(), name='list'),
            url(r'^new/$', views.CountryCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.CountryUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.CountryDelete.as_view(), name='delete'),
        ], namespace='Country')),

    url(r'^state/',
        include([
            url(r'^$', views.StateList.as_view(), name='list'),
            url(r'^new/$', views.StateCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.StateUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.StateDelete.as_view(), name='delete'),
        ], namespace='State')),

]

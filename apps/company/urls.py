from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^organization/',
        include([
            url(r'^$', views.OrganizationList.as_view(), name='list'),
            url(r'^new/$', views.OrganizationCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.OrganizationUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.OrganizationDelete.as_view(), name='delete'),
        ], namespace='Organization')),

    url(r'^subsidiary/',
        include([
            url(r'^$', views.SubsidiaryList.as_view(), name='list'),
            url(r'^new/$', views.SubsidiaryCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.SubsidiaryUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.SubsidiaryDelete.as_view(), name='delete'),
        ], namespace='Subsidiary')),

    url(r'^correlative/',
        include([
            url(r'^$', views.CorrelativeList.as_view(), name='list'),
            url(r'^new/$', views.CorrelativeCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.CorrelativeUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.CorrelativeDelete.as_view(), name='delete'),
        ], namespace='Correlative')),

]

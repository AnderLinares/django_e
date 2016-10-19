from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^vehicle/',
        include([
            url(r'^$', views.VehicleList.as_view(), name='list'),
            url(r'^new/$', views.VehicleCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.VehicleUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.VehicleDelete.as_view(), name='delete'),
        ], namespace='Vehicle')),

]

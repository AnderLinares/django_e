from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'',
        include([
            url(r'^vehicle/$', views.VehicleAPIListView.as_view(), name='vehicle'),
            url(r'^vehicle/(?P<pk>[0-9]+)/$', views.VehicleAPIView.as_view(), name='vehicle-detail'),
        ], namespace='api-vehicle')),


]

urlpatterns = format_suffix_patterns(urlpatterns)

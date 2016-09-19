from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import LabourAPIView, LabourAPIListView

urlpatterns = [
    url(r'^labour/$', LabourAPIListView.as_view(), name='api-labour'),
    url(r'^labour/(?P<pk>[0-9]+)/$', LabourAPIView.as_view(), name='api-labour-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

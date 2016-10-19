from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^module/',
        include([
            url(r'^$', views.ModuleList.as_view(), name='list'),
            url(r'^new/$', views.ModuleCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.ModuleUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.ModuleDelete.as_view(), name='delete'),
        ], namespace='Module')),

    url(r'^team/',
        include([
            url(r'^$', views.TeamList.as_view(), name='list'),
            url(r'^new/$', views.TeamCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.TeamUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.TeamDelete.as_view(), name='delete'),
        ], namespace='Team')),

    ]

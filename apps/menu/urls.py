from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^menu-permissions/',
        include([
            url(r'^$', views.MenuPermissionsList.as_view(), name='list'),
            url(r'^new/$', views.MenuPermissionsCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.MenuPermissionsUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.MenuPermissionsDelete.as_view(), name='delete'),
        ], namespace='MenuPermissions')),

    url(r'^menu/',
        include([
            url(r'^$', views.MenuList.as_view(), name='list'),
            url(r'^new/$', views.MenuCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.MenuUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.MenuDelete.as_view(), name='delete'),
        ], namespace='Menu')),

    url(r'^menu-item/',
        include([
            url(r'^$', views.MenuItemList.as_view(), name='list'),
            url(r'^new/$', views.MenuItemCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.MenuItemUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.MenuItemDelete.as_view(), name='delete'),
        ], namespace='MenuItem')),

    url(r'^team-menu/',
        include([
            url(r'^$', views.TeamMenuList.as_view(), name='list'),
            url(r'^new/$', views.TeamMenuCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.TeamMenuUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.TeamMenuDelete.as_view(), name='delete'),
        ], namespace='TeamMenu')),


    ]

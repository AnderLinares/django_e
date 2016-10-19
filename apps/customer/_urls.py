from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^user/',
        include([
            url(r'^$', views.UserList.as_view(), name='list'),
            url(r'^new/$', views.UserCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.UserUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.UserDelete.as_view(), name='delete'),
        ], namespace='User')),
]

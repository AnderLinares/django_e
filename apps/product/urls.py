from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^category/',
        include([
            url(r'^$', views.ProductCategoryList.as_view(), name='list'),
            url(r'^new/$', views.ProductCategoryCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.ProductCategoryUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.ProductCategoryDelete.as_view(), name='delete'),
        ], namespace='Category')),

    url(r'^subcategory/',
        include([
            url(r'^$', views.ProductSubCategoryList.as_view(), name='list'),
            url(r'^new/$', views.ProductSubCategoryCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.ProductSubCategoryUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.ProductSubCategoryDelete.as_view(), name='delete'),
        ], namespace='Subcategory')),

    url(r'^product/',
        include([
            url(r'^$', views.ProductList.as_view(), name='list'),
            url(r'^new/$', views.ProductCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.ProductUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.ProductDelete.as_view(), name='delete'),
        ], namespace='Product')),

]

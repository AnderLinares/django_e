from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    url(r'',
        include([
            url(r'^category/$', views.ProductCategoryAPIListView.as_view(), name='category'),
            url(r'^category/(?P<pk>[0-9]+)/$', views.ProductCategoryAPIView.as_view(), name='category-detail'),
        ], namespace='api-category')),

    url(r'',
        include([
            url(r'^subcategory/$', views.ProductSubCategoryAPIListView.as_view(), name='subcategory'),
            url(r'^subcategory/(?P<pk>[0-9]+)/$', views.ProductSubCategoryAPIView.as_view(), name='subcategory-detail'),
            url(r'^subcategory/(?P<category>[0-9]+)/category/$', views.ProductSubCategoryCategoryAPIListView.as_view(), name='subcategory-category'),

        ], namespace='api-subcategory')),

    url(r'',
        include([
            url(r'^product/$', views.ProductAPIListView.as_view(), name='product'),
            url(r'^product/(?P<pk>[0-9]+)/$', views.ProductAPIView.as_view(), name='product-detail'),
            url(r'^product/(?P<category>[0-9]+)/(?P<subcategory>[0-9]+)/$', views.ProductCategorySubCategoryAPIListView.as_view(), name='product-categoria-subcategory'),
        ], namespace='api-product')),

]

urlpatterns = format_suffix_patterns(urlpatterns)

from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^quotation_store/',
        include([
            url(r'^$', views.QuotationStoreList.as_view(), name='list'),
            url(r'^(?P<pk>[0-9]+)/$',  views.QuotationStoreDetailView.as_view(), name='detail'),
            url(r'^new/$', views.QuotationStoreCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/delete/$', views.QuotationStoreDelete.as_view(), name='delete'),
        ], namespace='QuotationStore')),

    ]

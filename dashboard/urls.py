from django.conf.urls import url, include

from .views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(),  name="index"),
    url(r'^admin/', include('core.urls')),
    url(r'^zone/', include('apps.zone.urls')),
    url(r'^product/', include('apps.product.urls')),
    url(r'^menu/', include('apps.menu.urls')),
    url(r'^team/', include('apps.team.urls')),
    url(r'^company/', include('apps.company.urls')),
    url(r'^supplier/', include('apps.supplier.urls')),
    url(r'^vehicle/', include('apps.vehicle.urls')),

    url(r'^customer/', include('apps.customer._urls')),

    url(r'^quotation/', include('apps.quotation.urls')),


    url(r'^api/', include('core.api.urls')),
    url(r'^api/', include('apps.zone.api.urls')),
    url(r'^api/', include('apps.product.api.urls')),
    url(r'^api/', include('apps.company.api.urls')),

    url(r'^api/', include('apps.supplier.api.urls')),

]

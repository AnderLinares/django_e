from django.conf.urls import url, include
from .views import ClientView, ClientCreateView, ClientEditView, ClientListView

client_patterns = ([
   url(r'^$', ClientView.as_view(), name="index"),
   url(r'^add/', ClientCreateView.as_view(), name="add"),
   url(r'^edit/', ClientEditView.as_view(), name="edit"),
   url(r'^list/', ClientListView.as_view(), name="list"),
], 'admin-client')

urlpatterns = [
    url(r'^client/', include(client_patterns)),

]


from django.conf.urls import url
from .forms import LoginForm
from .views import LogoutView, LoginView, IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(),  name="index"),

    url(r'^login/$', LoginView.as_view(),  name="auth_login"),
    url(r'^logout/$', LogoutView.as_view(), name='auth_logout'),
]

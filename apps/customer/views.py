from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.http import is_safe_url
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, RedirectView

from core.middleware.thread_user import CuserMiddleware
from core.mixins import AuthListView, AuthCreateView, AuthDeleteView, AuthUpdateView
from .forms import LoginForm, UserForm, UserProfileForm
from .models import UserProfile

User = get_user_model()


class LoginView(FormView):
    """
    Provides the ability to login as a user with a username and password
    """
    success_url = '/es/'
    form_class = LoginForm
    redirect_field_name = REDIRECT_FIELD_NAME
    template_name = 'registration/login.html'

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        request.session.set_test_cookie()
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()
        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        redirect_to = self.request.GET.get(self.redirect_field_name)
        if not is_safe_url(url=redirect_to, host=self.request.get_host()):
            redirect_to = self.success_url
        return redirect_to


class LogoutView(RedirectView):
    url = '/login/'
    permanent = False

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        CuserMiddleware.del_user()
        return super().get(request, *args, **kwargs)


"""
    User
"""


class UserList(AuthListView):
    template_name = 'dashboard/pages/customer/user/user_list.html'
    model = User
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("list User")
        return context


class UserCreation(AuthCreateView):
    template_name = 'dashboard/pages/customer/user/user_form.html'
    model = User
    success_url = reverse_lazy('User:list')
    form_class = UserForm

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)
        self.user_profile_form = UserProfileForm()
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        user_profile_form = UserProfileForm(self.request.POST, self.request.FILES)
        if form.is_valid() and user_profile_form.is_valid():
            return self.form_valid(form, user_profile_form)
        else:
            return self.form_invalid(form, user_profile_form)

    def form_valid(self, form, user_profile_form):
        self.object = form.save()
        user_profile_form.save(user=self.object, commit=False)
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, user_profile_form):
        self.form = form
        self.user_profile_form = user_profile_form
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form
        context["user_profile_form"] = self.user_profile_form
        return context


class UserUpdate(AuthUpdateView):
    template_name = 'dashboard/pages/customer/user/user_form.html'
    model = User
    success_url = reverse_lazy('User:list')
    form_class = UserForm

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)
        profile = UserProfile.objects.get(user=self.object)
        self.user_profile_form = UserProfileForm(instance=profile)
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        profile = UserProfile.objects.get(user=self.object)
        user_profile_form = UserProfileForm(
            self.request.POST, self.request.FILES, instance=profile)

        if form.is_valid() and user_profile_form.is_valid():
            return self.form_valid(form, user_profile_form)
        else:
            return self.form_invalid(form, user_profile_form)

    def form_valid(self, form, user_profile_form):
        self.object = form.save()
        user_profile_form.save(user=self.object, commit=False)
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, user_profile_form):
        self.form = form
        self.user_profile_form = user_profile_form
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form
        context["user_profile_form"] = self.user_profile_form
        return context


class UserDelete(AuthDeleteView):
    template_name = 'dashboard/pages/customer/user/user_confirm_delete.html'
    model = User
    success_url = reverse_lazy('User:list')

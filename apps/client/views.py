from json import loads

from django.contrib import messages
from django.views.generic import ListView
from django.views.generic import TemplateView

from core import constants as core_constants
from core.mixins import TemplateLoginRequiredMixin
from .forms import PersonForm
from .models import Person


class ClientView(TemplateLoginRequiredMixin, ListView):
    model = Person
    template_name = 'pages/client/client.html'
    context_object_name = "client_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Client List"
        return context


class ClientListView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/client/client_list.html'

    def get(self, request, *args, **kwargs):
        self.client_all = Person.objects.all()
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['client_list'] = self.client_all
        return context


class ClientCreateView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/client/client_form.html'

    def get(self, request, *args, **kwargs):
        self.form_client = PersonForm(auto_id='id_client_%s')
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        data = loads(request.body.decode('utf-8'))
        data_form_client = data['form']
        self.form_client = PersonForm(data=data_form_client, auto_id='id_client_%s')
        if self.form_client.is_valid():
            self.form_client.save()
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_client"] = self.form_client
        return context


class ClientEditView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/client/client_form.html'

    def get(self, request, *args, **kwargs):
        client = request.GET['person_id']
        self.client = Person.objects.get(pk=client)
        self.form_client = PersonForm(
            auto_id='id_client_%s', instance=self.client)
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        data = loads(request.body.decode('utf-8'))
        data_client_pk = data['form_pk']
        data_form_client = data['form']
        self.client = Person.objects.get(pk=data_client_pk)
        self.form_client = PersonForm(
            data_form_client, auto_id='id_client_%s', instance=self.client)
        if self.form_client.is_valid():
            self.form_client.save()
            messages.success(request, core_constants.STATUS_MSG_TAGS['success'])
        else:
            messages.error(request, core_constants.STATUS_MSG_TAGS['error'])
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_client'] = self.form_client
        context['form_pk'] = self.client.id
        context['btn_edit'] = core_constants.CODE_TEXT_EDIT
        return context

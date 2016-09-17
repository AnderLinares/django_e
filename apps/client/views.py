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
        self.person_all = Person.objects.all()
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['client_list'] = self.person_all
        return context


class ClientCreateView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/client/client_form.html'

    def get(self, request, *args, **kwargs):
        self.form_person = PersonForm(auto_id='id_person_%s')
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        data = loads(request.body.decode('utf-8'))
        data_form_person = data['form']
        self.form_person = PersonForm(data=data_form_person, auto_id='id_person_%s')
        if self.form_person.is_valid():
            self.form_person.save()
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_person"] = self.form_person
        return context


class ClientEditView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/client/client_form.html'

    def __init__(self, **kwargs):
        self.form_person = None
        self.person = None
        super().__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        person = request.GET['person_id']
        self.person = Person.objects.get(pk=person)
        self.form_person = PersonForm(
            auto_id='id_client_%s', instance=self.person)
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        data = loads(request.body.decode('utf-8'))
        data_person_pk = data['form_pk']
        data_form_person = data['form']
        self.person = Person.objects.get(pk=data_person_pk)
        self.form_person = PersonForm(
            data_form_person, auto_id='id_person_%s', instance=self.person)

        if self.form_person.is_valid():
            self.form_person.save()
            messages.success(request, core_constants.STATUS_MSG_TAGS['success'])
        else:
            messages.error(request, core_constants.STATUS_MSG_TAGS['error'])
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_person'] = self.form_person
        context['form_pk'] = self.person.id
        context['btn_edit'] = core_constants.CODE_TEXT_EDIT
        return context

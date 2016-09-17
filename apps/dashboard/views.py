from django.contrib.auth import get_user_model
from django.views import View
from django.views.generic import TemplateView

from core.mixins import TemplateLoginRequiredMixin

User = get_user_model()


class IndexView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/dashboard/index.html'

    def get(self, request, *args, **kwargs):
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

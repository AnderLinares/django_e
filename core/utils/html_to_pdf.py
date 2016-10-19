from io import StringIO

from django.http import HttpResponse
from django.template import Context
from django.template.defaultfilters import force_escape
from django.template.loader import get_template
from sx.pisa3.pisa_document import pisaDocument


class PDFQT(object):

    @staticmethod
    def render_to_pdf(template_src, context_dict):
        template = get_template(template_src)
        context = Context(context_dict)
        html = template.render(context)
        result = StringIO()
        pdf = pisaDocument(StringIO(html.encode("ISO-8859-1")), result)
        if not pdf.err:
            return HttpResponse(result.getvalue(), content_type='application/pdf')
        return HttpResponse('We had some errors<pre>%s</pre>' % force_escape(html))

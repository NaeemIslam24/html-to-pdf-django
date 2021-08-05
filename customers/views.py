from django.shortcuts import render, get_object_or_404
# for pdf-------------
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
# for pdf-------------
from django.views.generic import ListView
from .models import Customer


class CustomerListview(ListView):
    model = Customer
    template_name = 'main.html'


def customer_render_pdf(request, pk):

    customer = Customer.objects.get(id=pk)

    template_path = 'pdf2.html'
    context = {'customer': customer}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # it will take to downoad
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # it will display
    response['Content-Disposition'] = 'filename = "report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def render_pdf_view(request):
    template_path = 'pdf.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # it will take to downoad
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # it will display
    response['Content-Disposition'] = 'filename = "report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

from django.http import HttpResponse
from .models import Invoice
from datetime import datetime
from .router import Router



def upload_invoice(request):
    if(request.method == 'POST'):
        invoice = request.FILES['file']
        invoice_type = invoice.name.split('.')[-1]
        invoice_source = invoice.read().decode('utf-8')

        internal_invoice = Router.rout_invoices(invoice_source, invoice_type)

        invoice =Invoice.objects.create(
            stored_time = datetime.now(),
            invoice_source = invoice_source.replace('\r\n',''),
            internal_invoice = internal_invoice
            
        )
        
        return HttpResponse('Invoice Uploaded', status=200)
    else:
        return HttpResponse('Invalid Request',status=400)
        

    
           
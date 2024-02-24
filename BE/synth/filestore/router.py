from .converters import Converters

class Router:
    def rout_invoices(invoice_source, invoice_type):
        if invoice_type == 'csv':
            internal_invoice = Converters.csv_to_xml(invoice_source)
            internal_invoice = internal_invoice.replace('\n','')

        if invoice_type == 'xml':
            internal_invoice = Converters.xml_to_xml(invoice_source)
            internal_invoice = internal_invoice.replace('\r\n','')
    
        return internal_invoice
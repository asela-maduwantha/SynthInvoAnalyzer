import xml.etree.ElementTree as ET

class CommonHeaderCreator:
    
    @staticmethod
    def get_common_headers(headers=['bill_no','Bill No','Bill Number']):
        print("Before  :",headers)
        headerarray = [
            ["Invoice No", "invoice_number", "bill_no", "bill_number", "invoice_no", "Invoice Number", "Bill No", "Bill Number"],
            ["Invoice Date", "bill_date", "invoice_date", "Bill Date"],
            ["Customer Name", "customer_name", "Receiver Name"],
            ["Product", "product", "Item", "item"],
            ["Quantity", "quantity", "Qty", "qty"],
            ["Unit Price", "unit_price", "Price", "price"],
            ["Total", "total", "grand_total", "Grand Total"]
        ]

        for i in range(len(headers)):
            for j in range(len(headerarray)):
                for k in range(len(headerarray[j])):
                    if headers[i] == headerarray[j][k]:
                        headers[i] = headerarray[j][0]

        print("After  :",headers)
        return headers
  
   
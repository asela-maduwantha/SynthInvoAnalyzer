import csv
import xml.etree.ElementTree as ET
from .headerMapper import CommonHeaderCreator

class Converters:
    def csv_to_xml(csv_invoice):
    
        lines = csv_invoice.strip().split('\n')
        
        headers = CommonHeaderCreator.get_common_headers(lines[0].strip().split(','))
        
        root = ET.Element('Invoice')
        
        for line in lines[1:]:
            values = line.strip().split(',')
            row = ET.SubElement(root, 'row')
            for header, value in zip(headers, values):
                ET.SubElement(row, header).text = value
        
        xml_invoice = ET.tostring(root, encoding='unicode')

        return xml_invoice

    def xml_to_xml(xml_invoice):
        headers = set()
        try:
            root = ET.fromstring(xml_invoice)
            for element in root.iter():
                headers.add(element.tag)
    
            headers_list = list(headers)
            common_headers = CommonHeaderCreator.get_common_headers(headers_list)
            
         
            new_root = ET.Element("Invoice")  
            for header in common_headers:
                elements = root.findall(".//" + header)
                for element in elements:
                    new_root.append(element)

            reconstructed_xml = ET.tostring(new_root, encoding="unicode")
            return reconstructed_xml
            
        except ET.ParseError as e:
            print(f"Error parsing XML: {e}")

   


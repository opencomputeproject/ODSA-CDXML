from lxml import etree

xml_doc = etree.parse('BQ27426YZFT.xml')

xmlschema_doc = etree.parse('cdxml.xsd')
xmlschema = etree.XMLSchema(xmlschema_doc)

result = xmlschema.validate(xml_doc)


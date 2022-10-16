from lxml import etree

xmlschema_doc = etree.parse('cdxml.xsd')
xmlschema = etree.XMLSchema(xmlschema_doc)

xml_doc = etree.parse('BQ27426YZFT.xml')
result = xmlschema.validate(xml_doc)


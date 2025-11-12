import xml.etree.ElementTree as ET

import codecs
with codecs.open("fn8.xml",'rb','cp1251') as f:
    content = f.read()
    root = ET.fromstring(content)



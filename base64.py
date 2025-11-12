''' base_img = """

"""
base_img_bytes = base_img.encode('windows-1251')
with open('123.xml', 'wb') as file_to_save:
     decoded_image_data = base64.decodebytes(base_img_bytes)
     file_to_save.write(decoded_image_data)
'''

import xml.etree.ElementTree as ET

tree = ET.parse("fn8.ED")
root = tree.getroot()

for BankBIC in root.findall("Bank BIC")
	print(BankBIC.find("CorrespAcc").text)
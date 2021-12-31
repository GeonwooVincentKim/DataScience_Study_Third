import xml
import xml.etree.cElementTree as xml_e_tree
import json

with open("json_data.json") as json_data:
    get_json = json.load(json_data)
    print("{0}".format(get_json))

read_xml = xml_e_tree.Element("book_information")
print("XML Element Name -> {0}".format(read_xml))

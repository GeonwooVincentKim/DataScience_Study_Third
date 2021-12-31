import xml
import xml.etree.cElementTree as xml_e_tree
import json


# Get `JSON` data and write `XML` file
with open("json_data.json") as json_data:
    get_json = json.load(json_data)
    print("{0}".format(get_json))

read_xml = xml_e_tree.Element("book_information")
print("XML Element Name -> {0}".format(read_xml))

xml_e_tree.SubElement(read_xml, "title").text = get_json["title"]
xml_e_tree.SubElement(read_xml, "author").text = get_json["author"]
xml_e_tree.SubElement(read_xml, "publicationYear").text = str(get_json["publicationYear"])
xml_e_tree.SubElement(read_xml, "topics").text = get_json["topics"]

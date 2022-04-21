import xml.etree.ElementTree as ET

# load the xml
file = "/usr/share/X11/xkb/rules/evdev.xml"
tree = ET.parse(file)
root = tree.getroot()

# build a layout subtree
layout = ET.Element("layout")
cfgitm = ET.SubElement(layout, "configItem")
varlst = ET.SubElement(layout, "variantList")

name   = ET.SubElement(cfgitm, "name")
shdesc = ET.SubElement(cfgitm, "shortDescription")
fldesc = ET.SubElement(cfgitm, "description")
lnglst = ET.SubElement(cfgitm, "languageList")

ET.SubElement(lnglst, "iso639Id").text = "eng"
ET.SubElement(lnglst, "iso639Id").text = "fra"
ET.SubElement(lnglst, "iso639Id").text = "deu"

name.text   = "tarmak"
shdesc.text = "en"
fldesc.text = "Tarmak layout from: github.com/vjos/tarmak-layouts"

# add the new layout to the xml tree
root.find("layoutList").append(layout)
tree.write(file)


import xml.etree.ElementTree as ET
import xmltodict
import xml.dom.minidom as MINIDom
from inspect import getmembers, isclass, isfunction

# Display classes in ET module

print("\n","*" * 50,"\n") 
print("List of classes : ","\n")

for (name,member) in getmembers(ET, isclass):
    if not name.startswith("_"):
        print(name)

# Display functions in ET module

print("\n","*" * 50,"\n") 
print("List of functions : ","\n")

for (name,member) in getmembers(ET, isfunction):
    if not name.startswith("_"):
        print(name)

print("\n","*" * 50,"\n") 

# Playing around wit the config XML file pulled from the netconf script

getConfigResultsTree = ET.parse('config.xml')
root= getConfigResultsTree.getroot()

print(root)
print(type(root))
print(root.attrib)

print("\n","*" * 50,"\n") 

# Display classes in xmltodict module

print("\n","*" * 50,"\n") 
print("List of classes : ","\n")

for (name,member) in getmembers(xmltodict, isclass):
    if not name.startswith("_"):
        print(name)

# Display functions in xmltodict module

print("\n","*" * 50,"\n") 
print("List of functions : ","\n")

for (name,member) in getmembers(xmltodict, isfunction):
    if not name.startswith("_"):
        print(name)

# Display classes in xml.dom.minidom module

print("\n","*" * 50,"\n") 
print("List of classes : ","\n")

for (name,member) in getmembers(MINIDom, isclass):
    if not name.startswith("_"):
        print(name)

# Display functions in xml.dom.minidom module

print("\n","*" * 50,"\n") 
print("List of functions : ","\n")

for (name,member) in getmembers(MINIDom, isfunction):
    if not name.startswith("_"):
        print(name)
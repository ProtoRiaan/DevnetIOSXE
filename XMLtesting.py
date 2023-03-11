import xml.etree.ElementTree as ET
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

getConfigResultsTree = ET.parse('config.xml')
root= getConfigResultsTree.getroot()

print(root)
print(type(root))
print(root.attrib)

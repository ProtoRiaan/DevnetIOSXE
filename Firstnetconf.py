from ncclient import manager
#import lxml.etree as ET
import xmltodict
import xml.dom.minidom as MiniDom

router={"host":"sandbox-iosxe-latest-1.cisco.com", "port":"830",
        "username":"developer","password":"redmonitorioxdedicated34721"}

datafilter ="""
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
  </interfaces>
  """
#start the netconf session
m=manager.connect(host=router["host"],port=router['port'],username=router["username"],password=router["password"],hostkey_verify=False,device_params={'name':'csr'})

#  grab and print capabilities to file and screen

#capabilitiesFile = open('Capabilities.txt',"a")

for capability in m.server_capabilities:
        print('*' * 50,)
        print(capability)
       # capabilitiesFile.write('*' * 50)
       # capabilitiesFile.write("\n")
       # capabilitiesFile.write(capability)
       # capabilitiesFile.write("\n")

#capabilitiesFile.close()       

#  pull the running config as xml string
pulledconfig=m.get_config(source='running').xml

#  pull a yang schema as a string and printing to file
schema = m.get_schema('iana-if-type').xml
schemaFile = open('schema.txt','w')
schemaFile.write(schema)
schemaFile.close()

#  Printing some specific items using test filters.
#  Also using XMLtodict to grab the hostname as a string and saving in variable for later use

hostname = """
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
 <hostname>
 </hostname>
</native>
"""
print(m.get_config(source='running',filter=("subtree",hostname)))
routerHostnameXML = m.get_config(source='running',filter=("subtree",hostname)).xml
routerHostnameString = xmltodict.parse(routerHostnameXML)
routerHostnameValue = routerHostnameString['rpc-reply']['data']['native']['hostname']

version = """
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
 <version>
 </version>
</native>
"""
print(m.get_config(source='running',filter=("subtree",version)))

interfaceConfigured = """
<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
</interfaces>
"""

interfaceParseTest = m.get_config(source='running',filter=("subtree",interfaceConfigured)).xml
print(type(interfaceParseTest))
print(interfaceParseTest)

#  This part of the code is not working. ET cant parse the string with the Unicode element attached to the string. 
#  I can probably solve this by writing to a file and using the ET.parse(filename)
#  I know this is duplication of the config.xml but it is a smaller section and we are practicing working with XML.
#  I do need to do some more research and see if there is a better way to work with this. I am sure xmltodict can handle the parse, will test with that later

#interfaceParseTestXML = ET.fromstring(interfaceParseTest)
#print(type(interfaceParseTestXML))
#print(interfaceParseTestXML)

#for interface in m.get_config(source='running',filter=("subtree",interfaceConfigured)):
#        print(interface)


#  Converting the XML string to a dictionary object and printing out the individual configured interfaces and associated settings.

print('\n' * 5, "*" * 100)
print(f'      List of interfaces configurations on {routerHostnameValue} : \n')
print('*' * 100)
interfaceParseTestDict = xmltodict.parse(interfaceParseTest)
for interface in interfaceParseTestDict['rpc-reply']['data']['interfaces']['interface']:
        #print(interface)
        print(f'Interface Name : {interface["name"]}')
        try:
                print(f'Interface Description : {interface["description"]}')
        except:
                print('Interface Description : None')
        print(f'Interface Enabled : {interface["enabled"]}')
        try:                
                print(f'IP Address : {interface["ipv4"]["address"]}')
        except:
                print('IP Address : No IP address configured')
        print('*' * 100,'\n')

#  Section for writing config

#  Filter for writing config
writeLoopbackInterfaceFilter = '''
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
	<interface>
          <name>Loopback69</name>
       	  <name>Loopback69</name>
	  <description>Created by Badrobot using ncclient</description>	  
	  <enabled>true</enabled>	  
	</interface>
  </interfaces>
</config>
  '''

#  Write config to router

m.edit_config(
        target='running',
        config=writeLoopbackInterfaceFilter,
        default_operation='merge'
)




# setting filter for interface state

interfaceStateFilter = '''
<interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
</interfaces-state>
'''
#  Grabbing the running inteface state, converting to xmlminidom and print to screen
#  .get fails with no filter, the manager times out waiting for a response.

deviceStatusRawStr = m.get(filter=("subtree",interfaceStateFilter)).xml
deviceStatusDOM = MiniDom.parseString(deviceStatusRawStr)
print(deviceStatusDOM.toprettyxml(indent="  -"))


m.close_session()

#  write the running config that we pulled with .get_config to file on line 11

xmlOutputFile =open('config.xml','w')
xmlOutputFile.write(pulledconfig)
xmlOutputFile.close()
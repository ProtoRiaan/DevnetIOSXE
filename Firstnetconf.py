from ncclient import manager
import lxml.etree as ET

router={"host":"sandbox-iosxe-latest-1.cisco.com", "port":"830",
        "username":"developer","password":"redmonitorioxdedicated34721"}

datafilter ="""
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
  </interfaces>
  """
#start the netconf session
m=manager.connect(host=router["host"],port=router['port'],username=router["username"],password=router["password"],hostkey_verify=False,device_params={'name':'iosxe'})

#grab and print capabilities
for capability in m.server_capabilities:
        print('*' * 50)
        print(capability)

#pull the running config as xml string
pulledconfig=m.get_config(source='running').xml

#pull a yang schema as a string
schema = m.get_schema('ietf-interfaces').xml

#Printing some specific items using test filters.
hostname = """
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
 <hostname>
 </hostname>
</native>
"""
print(m.get_config(source='running',filter=("subtree",hostname)))

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

interfaceParseTest = m.get_config(source='running',filter=("subtree",interfaceConfigured))
print(type(interfaceParseTest))

#for interface in m.get_config(source='running',filter=("subtree",interfaceConfigured)):
#        print(interface)


m.close_session()

#write the running config that we pulled with .get_config to file on line 11
xmlOutputFile =open('config.xml','w')
xmlOutputFile.write(pulledconfig)
xmlOutputFile.close()


#cleaning up the schema xml object the we pulled with .get_shema on line 12 and printing to file
schemaFile = open('schema.txt','w')
schemaFile.write(schema)
schemaFile.close()

#Trying to clean up the xml config data
#can we grab just the 'Data' element
#configData=pulledconfig['data']
#configXML = ET.parse(pulledconfig)


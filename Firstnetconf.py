from ncclient import manager
from lxml import etree as ET

router={"host":"sandbox-iosxe-latest-1.cisco.com", "port":"830",
        "username":"developer","password":"redmonitorioxdedicated34721"}

m=manager.connect(host=router["host"],port=router['port'],username=router["username"],password=router["password"],hostkey_verify=False,device_params={'name':'iosxe'})
for capability in m.server_capabilities:
        print('*' * 50)
        print(capability)
pulledconfig=m.get_config(source='running').xml
schema = m.get_schema('ietf-interfaces')
m.close_session()

#prettyXML=ET.parse(pulledconfig)
#print(ET.tostring(prettyXML,pretty_print=True))

xmlOutputFile =open('config.xml','w')
xmlOutputFile.write(pulledconfig)
xmlOutputFile.close()

schemaFile = open('schema.txt','w')
schemaFile.write(str(schema))
schemaFile.close()



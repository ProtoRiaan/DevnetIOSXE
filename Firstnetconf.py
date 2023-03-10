from ncclient import manager
import xmltodict

router={"host":"sandbox-iosxe-latest-1.cisco.com", "port":"830",
        "username":"developer","password":"redmonitorioxdedicated34721"}

m=manager.connect(host=router["host"],port=router['port'],username=router["username"],password=router["password"],hostkey_verify=False,device_params={'name':'iosxe'})
for capability in m.server_capabilities:
        print('*' * 50)
        print(capability)
pulledconfig=m.get_config(source='running')
m.close_session()




from getpass import getpass
import requests
from pynxos.device import Device
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

nexus_ip = "153.92.39.248"
nxs_test = Device(host=nexus_ip, username="pyclass", password=getpass(),
                  transport='https', port=8443)

print nxs_test.show("show version")
print(nxs_test.facts)




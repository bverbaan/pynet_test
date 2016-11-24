from getpass import getpass

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

from pynxos.device import Device

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def main():

	switch_ip = "31.220.71.66"
 	username = 'pyclass'
	password = getpass()
	eth_inf = "Ethernet 2/2"
	int_ip = "10.1.4.6/30"
	peer_ip = "10.1.4.5"
	AS	= "10"

	configure_int = [
		"interface " + eth_inf,
		"ip address " + int_ip,
	]

	configure_bgp = [
		"license grace-period",
		"feature bgp",
		"router bgp " + AS,
		"neighbor {} remote-as {}".format(peer_ip, AS),
		"address-family ipv4 unicast",
	]

	nxs = Device(host=switch_ip, username=username, password=password, transport="https", port=8443)

	print "current config of Ethernet interface :"
	cmd = "show run int {}".format(eth_inf)
	print nxs.show(cmd, raw_text=True)

	print "\nConfiguring Ethernet Interface:"
    	nxs.config_list(configure_int)
   

	print "new config of Ethernet interface :"
        cmd = "show run int {}".format(eth_inf)
        print nxs.show(cmd, raw_text=True)


	print "current BGP config :"
	cmd = 'show run bgp'
	print nxs.show(cmd, raw_text=True)

	print "\nConfiguring BGP"
    	nxs.config_list(configure_bgp)

	print "new BGP config :"
        cmd = 'show run bgp'
        print nxs.show(cmd, raw_text=True)

	print "\nVerifying  BGP peers"
	cmd = 'show bgp session'
    	print nxs.show(cmd, raw_text=True)
    	
	print "\nSaving config..."
    	print nxs.save()

if __name__ == "__main__":
    main()


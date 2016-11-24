from getpass import getpass
from netmiko import ConnectHandler

def main():

	sw1_pass = getpass("enter switch password = ")
	pynet_sw1 = {
        	'device_type': 'arista_eos',
        	'ip':   '184.105.247.74',
        	'username': 'pyclass',
        	'password': sw1_pass,
	}

	cfg_commands = [
		'vlan 455',
		'name orange',
	]

	net_connect = ConnectHandler(**pynet_sw1)
	print "prompt is: "+ net_connect.find_prompt()

	output = net_connect.send_config_set(cfg_commands)
	print output

	output = net_connect.send_config_from_file("vlan_cfg.txt")
	print output

if __name__ == "__main__":
    main()

from getpass import getpass
from netmiko import ConnectHandler

def save_file(filename, show_run):
	with open(filename,"w") as f:
		f.write(show_run)

def main():
	rtr1_pass = getpass("enter router password:")
	sw1_pass = getpass("enter switch password:")
	
	pynet_rtr1 = {
        	'device_type': 'cisco_ios',
        	'ip':   '184.105.247.70',
        	'username': 'pyclass',
        	'password': rtr1_pass,
    	}

    	pynet_sw1 = {
        	'device_type': 'arista_eos',
        	'ip':   '184.105.247.72',
        	'username': 'pyclass',
        	'password': sw1_pass,
    	}
	for a_device in (pynet_rtr1, pynet_sw1):
		net_connect = ConnectHandler(**a_device)
		print "Prompt: " + net_connect.find_prompt()

		show_ver = net_connect.send_command("show version")
		print show_ver

		show_run = net_connect.send_command("show run")
		filename = net_connect.base_prompt + ".txt"
		print "saving show run file: {}".format(filename)
		save_file(filename, show_run)


if __name__ == "__main__":
	main()


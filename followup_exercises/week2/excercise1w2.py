#!/usr/bin/env python

from netmiko import ConnectHandler
from my_devices import device_list
import re

def check_vlan_exists(output):
    
    pattern = r"%.*not found in current VLAN database"
    return not bool(re.search(pattern, output))

def check_vlan_name(output, vlan_name):
    
    return vlan_name in output

def add_vlan(net_connect, vlan_id, vlan_name=''):
    cmd1 = "vlan " + str(vlan_id)
    cmds = [cmd1,]
    if vlan_name:
        cmd2 = "name " + vlan_name
        cmds.append(cmd2)
    return net_connect.send_config_set(cmds)


def Check_vlan_exists(output):

    pattern = r"%.*not found in current VLAN database"
    return not bool (re.search(pattern, output))

def main():

    new_vlans = [
        ('500', 'vlan11'),
        ('501', 'vlan22'),
        ('502', 'vlan33'),
    ]

    for a_device in device_list:
        net_conn = ConnectHandler(**a_device)
	print net_conn.find_prompt()
	for vlan_id, vlan_name in new_vlans:
            cmd = "show vlan id {}".format(vlan_id)
            print "Checking vlan_id: {}, vlan_name: {}".format(vlan_id, vlan_name)
	    output = net_conn.send_command(cmd)
	    print output
	    vlan_exists = check_vlan_exists(output)
	    print "vlan exists is {}".format(vlan_exists) 
	    vlan_name_correct = check_vlan_name(output, vlan_name)
	    print "vlan name correct is {}".format(vlan_name_correct)
	    if not vlan_exists or not vlan_name_correct:
		print "Updating and/or adding vlan"
		output = add_vlan(net_conn, vlan_id, vlan_name)
                print "Done"
            else:
                print "VLAN exists and has correct name"

	print

if __name__ == "__main__":
    main()



#!/usr/bin/env python

from netmiko import ConnectHandler
from my_devices import device_list
import re
import threading
from Queue import Queue
from datetime import datetime

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

def ssh_conn(a_device, my_queue):

    new_vlans = [
        ('500', 'vlan11'),
        ('501', 'vlan22'),
        ('502', 'vlan33'),
    ]

    net_conn = ConnectHandler(**a_device)
    device_name = net_conn.base_prompt
    output_dict = {device_name: {}}

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
		output_dict[device_name][vlan_id] = 'changed'
                
            else:
                output_dict[device_name][vlan_id] = 'unchanged'
    my_queue.put(output_dict)

    print

def main():

    my_queue = Queue()

    for a_device in device_list:
        my_thread = threading.Thread(target=ssh_conn, args=(a_device, my_queue))
        my_thread.start()

    main_thread = threading.currentThread()
    for some_thread in threading.enumerate():
        if some_thread != main_thread:
            some_thread.join()

    while not my_queue.empty():
        print my_queue.get()

start_time = datetime.now()
	
if __name__ == "__main__":
    main()

end_time = datetime.now()

total_time = end_time - start_time

print total_time

#!/usr/bin/env python

import csv
from netmiko import ConnectHandler

#def connection(device_name)

def main():

	file_name = 'test_net_devices.csv'
	with open(file_name) as f:
    		read_csv = csv.DictReader(f)
    		for entry in read_csv:
        		host=entry['host']
			device_name=entry.pop('device_name')
			device_type=entry['device_type']
			print device_name, host , device_type
			net_conn = ConnectHandler(**entry)
			print(net_conn.find_prompt())


if __name__ == "__main__":
    main()

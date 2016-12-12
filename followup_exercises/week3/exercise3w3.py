#!/usr/bin/env python

import csv
import yaml

def main():

	yaml_file = 'myfile.yml'
    	file_name = 'write_net_devices.csv'

	with open(yaml_file) as f:
		yaml_output = yaml.load(f)

	with open(file_name, "wt") as f:
    		writer = csv.writer(f)
    		writer.writerow(('device_name', 'device_type', 'host', 'username', 'password'))
		for device in yaml_output:
			writer.writerow((device['device_name'], device['device_type'], device['host'], device['username'], device['password']))


if __name__ == "__main__":
    main()



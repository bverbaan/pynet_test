#!/usr/bin/env python

import csv

def main():

	file_name = 'test_net_devices.csv'
	with open(file_name) as f:
    		read_csv = csv.DictReader(f)
    		for entry in read_csv:
        		print entry



if __name__ == "__main__":
    main()

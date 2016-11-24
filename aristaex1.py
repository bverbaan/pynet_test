#!/usr/bin/env python
from pprint import pprint
import pyeapi

def main():
	pynet_sw = pyeapi.connect_to("pynet-sw4")
	output = pynet_sw.enable("show ip route") 


	print output

	output = output[0]
    	output = output['result']['vrfs']['default']

	print 
	print output

	routes = output['routes']
    	print "\n{:>15} {:>15} {:>15}".format("prefix", "interface", "next_hop")
    	filler = "-" * 15
    	print "{:>15} {:>15} {:>15}".format(filler, filler, filler)
    	for prefix, attr in routes.items():
        	intf_nexthop = attr['vias'][0]
        	interface = intf_nexthop.get('interface', 'N/A')
        	next_hop = intf_nexthop.get('nexthopAddr', 'N/A')
        	print "{:>15} {:>15} {:>15}".format(prefix, interface, next_hop)
    	print




if __name__ == "__main__":
    main()

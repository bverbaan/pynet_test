#!
ip_addr = raw_input("please enter IP address")
ip_addr2 = ip_addr.split(".")

print "{:<12} {:<12} {:<12} {:<12}".format(*ip_addr2)


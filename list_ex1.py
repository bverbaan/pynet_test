ip_addr = raw_input('please enter ip address =')
ip_list = ip_addr.split(".")
ip_list[-1] = '0'
print "{:>10} {:>10} {:>10} {:>10}".format(*ip_list)

a1 = bin(int(ip_list[0]))
a2 = bin(int(ip_list[1]))
a3 = bin(int(ip_list[2]))
a4 = bin(int(ip_list[3]))
print "{:>10} {:>10} {:>10} {:>10}". format(a1, a2, a3, a4)

network_device = {
	'ip_addr': "192.168.0.1",
	'username' : 'administrator',
	"password": "cisco",
	"vendor": "Cisco",
	"model": "3845",

}

print
for a, b in network_device.items():
	print a,b

network_device["password"] = "Juniper"
network_device["secret"] = "secret"

print
for a,b in network_device.items():
	print a,b


device_type = network_device.get('device_type', 'cisco-ios')
print "device type {}".format(device_type)



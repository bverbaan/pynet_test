#!/usr/bin/env python
import pprint

user = {
        'name': 'John Doe',
        'phone': '32-14-607080',
        'address': 'TrammesandLei 36',
	'postalcode': '2000',
	'city': 'Antwerp',
	'country': 'Belgium',
    }

print
pprint.pprint(user)

print
print "just printing the dictionary keys"

for k in user:
	print k


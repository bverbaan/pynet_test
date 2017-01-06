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
print "{name:15} {phone:15} {address:30} {postalcode:15} {city:15} {country:15}".format(**user)


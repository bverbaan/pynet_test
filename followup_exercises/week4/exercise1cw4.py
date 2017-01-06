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

city = user.pop('city')
print "removing city " + city
print
pprint.pprint(user)

print
if not user.get('city'):
        user['city'] = 'Antwerp'
print
pprint.pprint(user)


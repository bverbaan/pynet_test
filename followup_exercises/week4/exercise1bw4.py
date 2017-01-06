#!/usr/bin/env python


user = {
        'name': 'John Doe',
        'phone': '32-14-607080',
        'address': 'TrammesandLei 36',
	'postalcode': '2000',
	'country': 'Belgium',
    }
print user['name']
print user['phone']
print user['address']
print user['postalcode']
print user['country']

try:
        print user['city']
except KeyError:
        user['city'] = 'Antwerp'
        print user['city']	

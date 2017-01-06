#!/usr/bin/env python

my_list = ['1', 'sun', 666, 'help', 45, "M5", 'wheel']

my_list.append('8th element')


for i,entry in enumerate(my_list):
        print i, entry
print
print "changing elements"
print
my_list[2]='earth'

my_list[-1]='8th element bis'

for i,entry in enumerate(my_list):
        print i, entry





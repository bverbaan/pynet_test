#!/usr/bin/env python

my_list = ['1', 'sun', 666, 'help', 45, "M5", 'wheel']

my_list.append('8th element')


for i,entry in enumerate(my_list):
        print i, entry
print
print "changing elements"
print
my_list.pop()
my_list.pop(0)
my_list.pop(2)


for i,entry in enumerate(my_list):
        print i, entry

l=len(my_list)

print "list length = ", l

new_list = ['aaa', 2 , 306]

my_list.extend(new_list)

for i,entry in enumerate(my_list):
        print i, entry


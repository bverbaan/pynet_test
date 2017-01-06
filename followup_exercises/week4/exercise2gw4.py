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

print
print "adding new list"
my_list.extend(new_list)

for i,entry in enumerate(my_list):
        print i, entry
print
print "adding element between pos 1 and 2"
print
my_list.insert(1, "testpos2")

for i,entry in enumerate(my_list):
        print i, entry

print
print "print element 1-4"
print my_list[0:4]

print "create new list with 5 last elements"
new_list2 = my_list[-5:]

print new_list2



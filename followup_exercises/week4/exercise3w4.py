#!/usr/bin/env python

def function1():
    print "hello world"

def function2(x,y):
    print "hello world function2, x = {}, y = {}".format(x,y)

def function3(x,y,z=10):
    print "hello world function3, x = {}, y = {}, z = {}".format(x,y,z) 

def function4(x,y,z):
     return x + y + z

def function5(my_func):
    my_func()
    my_func()
    my_func()

def main():

    print
    print "Exercise 3a"
    function1()
    
    print
    print "Exercise 3b"
    function2("a1", 3)

    print    
    print "Exercise 3c"
    function3(1,2)
    function3(1,2,3)
    function3(x=51, y=62, z=73)
    function3(1, y=2, z=7)	
    try:
        function3(7, 9, y=8)
    except TypeError:
        print "Error"
    print

    print "Exercise 3d"
    my_list = [55,66,77]
    function3(*my_list)
    print

    print "Exercise 3e"
    my_dict = {'x':11, 'z':33, 'y':22}
    function3(**my_dict)
    print

    print "Exercise 3f"
    print "total x+y+z =", function4(33,56,32)
    print "total x+y+z =", function4('aaa', 'bbb', 'ccc')
    print

    print "Exercise 3g"
    function5(function1)

if __name__ == "__main__":
    main()

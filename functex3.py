def my_function(x, y, z=20):	
	return x + y + z

my_list = [33,66,99]

my_dict = {
	'x':133,
	'y':266,
	'z':399,
}


return_value = my_function(1,2,3)

print "using positional aruments: {}".format(return_value)

return_value = my_function(x=100, y=200)

print "using named arguments: {}".format(return_value)

return_value = my_function(1, y=2, z=3)

print "using pos and named arguments {}".format(return_value)

return_value = my_function(x='string1', y='string2', z='string3')

print "using strings {}".format(return_value)

return_value = my_function(x=[1,2,3],y=[4,5,6],z=[7,8,9])

print "using lists {}".format(return_value)

return_value = my_function(*my_list)

print "using *arguments {}".format(return_value)

return_value = my_function(**my_dict)

print "using kwargs {}".format(return_value)
 

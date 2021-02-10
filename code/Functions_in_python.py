#functions in python

#default function
# def my_function():
#     print("this is function!!")
#
# my_function()


#parametrized function

# def mfunction(name):
#     print(name)
# mfunction("abdul")
# mfunction("gaffar")
# mfunction("Shaikh")

#arbitrary parameter if the no of parameter is unknown just add * before variable

# def my_function(*name):
#     print(name[4])
# my_function("abdul","gaffar","nazeer","shaikh","aisha bi")
#

# Keyword Arguments
# You can also send arguments with the key = value syntax.
#
# This way the order of the arguments does not matter.

# def my_function(fname,mname,lname):
#     print("first name is : ",fname," middle name is : ",mname," last name is : ",lname)
# #my_function("abdul gaffar","nazeer","shaikh")
# my_function( fname="abdul gaffar",mname= "nazeer", lname="shaikh")

#If the number of keyword arguments is unknown, add a double ** before the parameter name:
# def my_function(**name):
#     print("his first name is : ",name["fname"],"last name is : ",name["lname"])
# my_function(fname="gaffar",lname="shaikh")


# Default Parameter Value
# The following example shows how to use a default parameter value.
#
# If we call the function without argument, it uses the default value:
#
# Example


# def my_function(country="sweden"):
#     print(country)
# my_function("india")
# my_function()
# my_function("canada")
#

#
# Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
#
# E.g. if you send a List as an argument, it will still be a List when it reaches the function:

# def myfunction(food):
#     for x in food:
#         print(x)
# fruits=["appale","banana","cherry","lemon","litchi","etc"]
# myfunction(fruits)


#returninig for functions

# def my_functions(x):
#     return 2*x
#
# for x in range(1,11):
#     print(my_functions(x))
#

#use pas keyword when there is no content in function
# def my_function():
#     pass
# my_function()

# Recursion
# Python also accepts function recursion, which means a defined function can call itself.
#
# Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.
#
# The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.
#
# In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).
#
# To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.
#

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

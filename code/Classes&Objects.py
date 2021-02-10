# class demo:
#     x=100
#
# p=demo()
# print(p.x)

#define a class and def constructor
#
# The __init__() Function
# The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
#
# To understand the meaning of classes we have to understand the built-in __init__() function.
#
# All classes have a function called __init__(), which is always executed when the class is being initiated.
#
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:


class person:
    def __init__(self ,fname,lname):
        self.fname=fname
        self.lname=lname


p1=person("gaffar","shaikh")
#change value in the object
#p1.lname="ladale"
# print(p1.fname," : ",p1.lname)


#
# Note: The __init__() function is called automatically every time the class is being used to create a new object.
#self isused to indicate the current instance of a class


#del object properties
# del p1.fname
# del p1
print(p1.fname," : ",p1.lname)



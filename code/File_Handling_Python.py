# File handling is an important part of any web application.
#
# Python has several functions for creating, reading, updating, and deleting files.
#
# File Handling
# The key function for working with files in Python is the open() function.
#
# The open() function takes two parameters; filename, and mode.
#
# There are four different methods (modes) for opening a file:
#
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
#
# "a" - Append - Opens a file for appending, creates the file if it does not exist
#
# "w" - Write - Opens a file for writing, creates the file if it does not exist
#
# "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode
#
# "t" - Text - Default value. Text mode
#
# "b" - Binary - Binary mode (e.g. images)


# Syntax
# To open a file for reading it is enough to specify the name of the file:

#read a file using a read function
#f=open("demo.txt","r")
#print(f.read())

#read a specific part of a file
#print(f.read(10))

#read line of a file
# print(f.readline())
# print(f.readline())
# print(f.readline())

# for x in f:
#     print(x)

# f=open("demo.txt","a")
# f.write("\nand this is a last line")
# f.close()
# f=open("demo.txt","r")
# print(f.read())


#overwrite the whole file
# f=open("demo.txt","w")
# f.write("this is new content!!!")
# f.close()
# f=open("demo.txt","r")
# print(f.read())

#Note: the "w" method will overwrite the entire file.


# Create a New File
# To create a new file in Python, use the open() method, with one of the following parameters:
#

#
# "a" - Append - will create a file if the specified file does not exist
#


# "x" - Create - will create a file, returns an error if the file exist
# f=open("demo2.txt","x")

# "w" - Write - will create a file if the specified file does not exist
#f=open("demo2.txt","w")
import os


# if os.path.exists("demo.txt"):
#     os.remove("demo.txt")
#     print("if executed!!!")
# else:
#     os.rmdir("trash")
#     print("else executed")

#
# f=open("demo.txt","x")
# f.write("hello this is new file created")

# f=open("demo.txt","w")
# f.write("this is new content!!!")
# f.close()

f=open("demo.txt","a")
f.write("\nand this is a seperate line attaching in that file!!!")
f=open("demo.txt","r")
print(f.read())
f.close()





#NumPy is a python library used for working with arrays.
# It also has functions for working in domain of linear algebra, fourier transform, and matrices.
#
# NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely.
#
# NumPy stands for Numerical Python.
# Why Use NumPy ?
# In Python we have lists that serve the purpose of arrays, but they are slow to process.
#
# NumPy aims to provide an array object that is up to 50x faster that traditional Python lists.
#
# The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.
#
# Arrays are very frequently used in data science, where speed and resources are very important.
#
# Data Science: is a branch of computer science where we study how to store, use and analyze data for deriving information from it.
#
# Why is NumPy Faster Than Lists?
# NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.
#
# This behavior is called locality of reference in computer science.
#
# This is the main reason why NumPy is faster than lists. Also it is optimized to work with latest CPU architectures.
#
# Which Language is NumPy written in?
# NumPy is a Python library and is written partially in Python, but most of the parts that require fast computation are written in C or C++.



import numpy as np

# arr=np.array([1,2,3,4,5])
# print(arr)
# print(arr[0:3])
# print(arr[::-1])
# print(arr[-1])
#
#
# #check numpy version
# print(np.__version__)
#
# #numpy creating arrays
# print(type(arr))

# 0-D Arrays
# 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
#
# Example
# Create a 0-D array with value 42


# ar1=np.array(42)
# print(ar1)
#print(ar1.size)


# ar2=np.array([[1,2,3,4,5],[6,7,8,9,10]])
# #access the element of first array of 2d array
# print(ar2[0])
#
# #acces the elements of first array
# print(ar2[0][4])
# print(ar2[1][-1])
# #reversing the 2nd array
# print(ar2[1][::-1])
#


#creating a 3D array

# ar3=np.array([[[1,2],[3,4],[5,6],[7,8],[9,10]]])
# print(ar3[0][4][1])


#check dimensions of array

a=np.array(42)
# b=np.array([1,2,3,4,5], ndmin=5)#creating five dimensionl array
# c=np.array([[1,2],[3,4]])
# d=np.array([[[1,2],[3,4],[5,6]]])

# print(a.ndim)
# print(b.ndim)#creating five dimensionl array
# print(c.ndim)
# print(d.ndim)

###################################numpy array indexing##################################################


b=np.array([1,2,3,4,5])#creating five dimensionl array
c=np.array([[1,2],[3,4]])
d=np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# print(b[0])
# print(c[1,0])
# print(d[0,0,-1])

###################################numpy array slicing##################################################

#
# b=np.array([1,2,3,4,5,6,7])#creating five dimensionl array
# print(b[0:4])
# #slice  from 2nd to last element
# print(b[1:])
# #slice  from beginnig  to 4th (4th item excluded)
# print(b[:4])
# #negative slicing
# print(b[-3:-1])
# #return every element from index 1 to 5
# print(b[1:5:2])
# print(b[::2])


#slicinig 2D arrays

#c=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(c[1,0:2])
# # print(c[0:3,2])
# print(c[0:3,0:3])


###################################Datatypes in numpy##################################################

# string
# integer
# boolean
# float
# complex


#check datataype of array

#integer array
#c=np.array([[1,2,3],[4,5,6],[7,8,9]])
#float array
#d=np.array([[1.2,2.5,3.5],[4.0,5.0,6.2],[7.8,8.6,9.4]])
#print(d.dtype)
#string array
#s=np.array([['a','b','c'],['d','e','f']])
#print(s.dtype)

#craeting float array to integer array
# newarr=d.astype('i')
# arrr=c.astype('f')
# print(newarr.dtype)
# print(arrr.dtype)
#
# print(newarr)
#print(arrr)

################################numpy array copy vs view##################################
# The Difference Between Copy and View
# The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.
#
# The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.
#
# The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.


arr=np.array([1,2,3,4,5])
# x=arr.copy()
# #print(x[::4])
# arr[0]=42
# print(arr)

##view example##




#in view changes are reflected after the array is copieddd!!!
# x=arr.view()
# #x=arr.copy()
# arr[0]=42
# print(arr)
# print(x)

#Check if Array Owns it's Data
arr=np.array([1,2,3,4,5])

# x=arr.copy()
# y=arr.view()
#
# print(x.base)
# print(y.base)


########################################Array Shape###############################################
# arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])

# print(arr.shape)
#
# d=np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
#
# print(d.shape)
#

########################################numpy array reshape#########################################
#convert from 1d to 2d array

ars=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newar=ars.reshape(4,3)
# #print(newar)
# print(newar[0][3])
#print(newar)


#Reshape From 1-D to 3-D
# newar=ars.reshape(3,2,2)
# print(newar)


#flattering the array
# it means converting any dimensional array to 1d array

arr = np.array([[1, 2, 3], [4, 5, 6],[3,23,23,]])

#use -1 in reshape function to convert
#newarr = arr.reshape(-1)
#print(newarr)
# note: There are a lot of functions for changing the shapes of arrays in numpy
# flatten, ravel and also for rearranging the elements rot90, flip, fliplr, flipud etc.
# These fall under Intermediate to Advanced section of numpy.




##############################################NumPy Array Iterating###################################
# Iterating Arrays
# Iterating means going through elements one by one.
#
# As we deal with multi-dimensional arrays in numpy, we can do this using basic for loop of python.
#
# If we iterate on a 1-D array it will go through each element one by one.
#
# Example
# Iterate on the elements of the following 1-D array:




#use for loop to iterate 1D array

# ar=np.array([1,2,3,4,5])
# for x in ar:
#     print(x)

#Iterating 2-D Arrays
#In a 2-D array it will go through all the rows.


# ar=np.array([[1,2,3,4,5],[6,7,8,9,10]])
# for x in ar:
#     for y in x:
#         print(y)


# Iterating 3-D Arrays
# In a 3-D array it will go through all the 2-D arrays.
#
# Example
# Iterate on the elements of the following 3-

# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
#
# for x in arr:
#   #for y in x:
#       #for z in y:
#           print(x)
#           print(arr.ndim)

#iterating the array through nditer()

# arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
#
# arr1=np.array([[1,2,3,4,5],[6,7,8,9,10]])
# for x in np.nditer(arr1):
#   print(x)
#   print(arr1.ndim)
#
#

#########################################numpy  array join###########################################

#join 1d array
# ar1=np.array([1,2,3,4,5])
# ar2=np.array([6,7,8,9,10])
# ar3=np.concatenate((ar1,ar2))
#print(ar3)
#join 2d array
# ar1=np.array([[1,2],[3,4]])
# ar2=np.array([[5,6],[7,8]])
# ar3=np.concatenate((ar1,ar2),axis=1)
# print(ar3)


# Joining Arrays Using Stack Functions
# Stacking is same as concatenation, the only difference is that stacking is done along a new axis.
#
# We can concatenate two 1-D arrays along the second axis which would result in putting them one over the other, ie. stacking.
#
# We pass a sequence of arrays that we want to join to the concatenate() method along with the axis.
# If axis is not explicitly passed it is taken as 0

# ar1=np.array([1,2,3])
# ar2=np.array([4,5,6])
# ar3=np.stack((ar1,ar2),axis=1)
# print(ar3)



# Stacking Along Rows
# # NumPy provides a helper function: hstack() to stack along rows.
# ar1=np.array([1,2,3])
# ar2=np.array([4,5,6])
# #ar3=np.hstack((ar1,ar2))    horizontally
# ar3=np.vstack((ar1,ar2))#vertically
# print(ar3)

################################NumPy Splitting Array##############################
# Splitting NumPy Arrays
# Splitting is reverse operation of Joining.
# Joining merges multiple arrays into one and Splitting breaks one array into multiple.
# We use array_split() for splitting arrays,
# we pass it the array we want to split and the number of splits.

#split the array in 3parts

# arr2=np.array([1,2,3,4,5,6,7,8,9])
# newar=np.array_split(arr2,3)
# print(newar[-1])
#

# Splitting 2-D Arrays
# Use the same syntax when splitting 2-D arrays.
#
# Use the array_split() method,
# pass in the array you want to split and the number of splits you want to do.


# arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
# newarr = np.array_split(arr, 3)
# print(newarr)


#Note: Similar alternates to vstack() and dstack() are available as vsplit() and dsplit().

######################################NumPy Searching Arrays##########################################

# Searching Arrays
# You can search an array for a certain value, and return the indexes that get a match.
#
# To search an array, use the where() method.
#
# Example
#


ar=np.array([1,2,3,4,5,4,8,4,7,4])
#To search an array, use the where() method.

# x=np.where(ar==4)
# print(x)



#find index where value id divisible by 2

# z=np.where(ar%2==0)
# #z=np.where(ar%2==0)
# print(z)

#
# Search Sorted
# There is a method called searchsorted() which performs a binary search in the array,
# and returns the index where the specified value would be inserted to maintain the search order.

# ar=np.array([1,2,3,4])
# # k=np.searchsorted(ar,4)
# # print(k)
#
# #search from right side
#
# # k=np.searchsorted(ar,1,side='right')
# # print(k)
#
# ar=np.array([1,2,3,4,5])
# k=np.searchsorted(ar,[1,3,5])
# print(k)

############################numpy array sort#####################################################
#
# Sorting Arrays
# Sorting means putting elements in a ordered sequence.
# Ordered sequence is any sequence that has an order corresponding to elements, like numeric
# or alphabetical, ascending or descending.
# The NumPy ndarray object has a function called sort(), that will sort a specified array.


ar=np.array([5,3,4,1,2])
# print(np.sort(ar))
#
# #sort aplhabetically
#
# ar1=np.array(['banana','chikoo','apple','donut'])
# print(np.sort(ar1))

#Sorting a 2-D Array
#If you use the sort() method on a 2-D array, both arrays will be sorted:

# ar=np.array([[3,2,1],[6,5,4]])
# print(np.sort(ar))

#####################################NumPy Filter Array###############################################

# Filtering Arrays
# Getting some elements out of an existing array and creating a new array out of them is called filtering.
#
# In NumPy, you filter an array using a boolean index list.


ar=np.array([5,10,15,20])
# x=[True,False,False,True]
# newar=ar[x]
# print(newar)

filter_list=[]

for elements in ar:
    if elements>10:
        filter_list.append(elements)


#newarr=ar(filter_list)
# print(filter_list)
#
# x=np.array(filter_list)
# print(x)
#####################################random#######################################################

#
# What is a Random Number?
# Random number does NOT mean a different number every time. Random means something that can not be predicted logically.
#
# Pseudo Random and True Random.
# Computers work on programs, and programs are definitive set of instructions. So it means there must be some algorithm to generate a random number as well.
#
# If there is a program to generate random number it can be predicted, thus it is not truly random.
#
# Random numbers generated through a generation algorithm are called pseudo random.
#
# Can we make truly random numbers?
#
# Yes. In order to generate a truly random number on our computers we need to get the random data from some outside source. This outside source is generally our keystrokes, mouse movements, data on network etc.
# We do not need truly random numbers, unless its related to security (e.g. encryption keys) or the basis of application is the randomness (e.g. Digital roulette wheels).
# In this tutorial we will be using pseudo random numbers.
# Generate Random Number
# NumPy offers the random module to work with random numbers.


from numpy import random
# x=random.randint(100)
# y=random.rand()
# print(x)
# print(y)

#generatye random array


# x=random.randint(100,size=(3,5))
# print(x)
#
# y=random.rand(2,1)
# print(y)

# k=random.choice([1,2,3,4,5],size=(3,4))
# print(k)


#################################NumPy ufuncs#############################################


import numpy as np
print(type(np.add))



thislist=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thiscity=["mumbai", "delhi", "kolkata", "rajasthan", "GOA", "KARNATAKA", "Gukarat"]
# print(thislist)
#
# print(thislist[0:3])
#
# print(thislist[-1])
# print(thislist[:-2])
#
# print(thislist[:2])
#
# print(thislist[1:])
#
# print(thislist[-4:-1])
#
# thislist[1]="hawana"
# print(thislist)

# for x in thislist,thiscity:
#     print(x)

#
#
# print(len(thislist))
# print(len(thiscity))

# thiscity.append("kashmir")
# print(thiscity)
# thiscity.insert(0,"maharashtra")
# print(thiscity)
#
# print(thiscity)
# thiscity.pop()
# print(thiscity)
# del thiscity[0]
# print(thiscity)
#
my_city=thiscity.copy()
# print(my_city)
#
list2=thiscity+my_city
# print(list2)


num=[0,1,2,3,4,5,6,7,8,9,10]

for x in num:
    list2.append(x)
    print(list2)


# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list


#remove duplicate items from list

l1=['a','b','a','c','d','e','c']
myl1=list(dict.fromkeys(l1))
print(myl1)

x="hello"
print(x[0])

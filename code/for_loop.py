# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
#
# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
#
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc


#
# for x in "banana":
#     print(x)

# fruits=["guawa","pineapple","kiwi","mango","apple"]
# for x in fruits:
#     if x == "kiwi":
#         #continue
#         break
#     print(x)
#

#range function
#Note that range(6) is not the values of 0 to 6, but the values 0 to 5

# for x in range(10):
#     print(x)
#
#
# for x in range(1,11):
#     print(x)

#Increment the sequence with 3 (default is 1):
# for x in range(1,11,3):
#     print(x)
#




for x in range(1,11):
    for y in range(11,21):
        print(x,":",y)
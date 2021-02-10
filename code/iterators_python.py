# Python Iterators
# An iterator is an object that contains a countable number of values.
#
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
#
# Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
#
# Iterator vs Iterable
# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
#
# All these objects have a iter() method which is used to get an iterator:
#
# Example
# Return an iterator from a tuple, and print each value:

#simple iterator

mytuple=("gaffar","nazeer","shaikh")
myiter=iter(mytuple)

print(next(myiter))
print(next(myiter))
print(next(myiter))

#even string is iterable
str="pineapple"
myit=iter(str)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


# The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
#
# The __next__() method also allows you to do operations, and must return the next item in the sequence.


class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

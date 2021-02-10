# JSON is a syntax for storing and exchanging data.
#
# JSON is text, written with JavaScript object notation.
#
# JSON in Python
# Python has a built-in package called json, which can be used to work with JSON data.
#

import json
#simple json example
# x='{ "name":"john","age":30,"city":"mumbai"}'
#
# y=json.loads(x)
# print(y["city"])
#
#

x ={
  "name": "John",
  "age": 30,
  "city": "New York"
}
#python to json
y=json.dumps(x)
print(y)

# You can convert Python objects of the following types, into JSON strings:
#
# dict
# list
# tuple
# string
# int
# float
# True
# False
# None

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


#When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:
#
# Python	JSON
# dict	Object
# list	Array
# tuple	Array
# str	String
# int	Number
# float	Number
# True	true
# False	false
# None	null


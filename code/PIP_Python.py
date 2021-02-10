# What is PIP?
# PIP is a package manager for Python packages, or modules if you like.

#install any package eg: pip install camelcase
#uninstall any package eg: pip install camelcase

#list all the packages :pip list


import camelcase
#capitalize first letter of every word
c=camelcase.CamelCase()

x="the camel hump example"
print(c.hump(x))
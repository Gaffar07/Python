#Create a class named Person, with firstname and lastname properties, and a printname method
class demo:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def printname(self):
        print("name is ",self.name," age is : ",self.age)


# p1=demo("gaffar",36)
#
# p1.printname()
#
#
# class child(demo):
#     pass



# c=child("john",50)
# c.printname()


class test(demo):
    def __init__(self,name,age,gradyear):
            super().__init__(name,age)
            self.gradyear=2019
            print(gradyear)
p1=test("aka",12,1994)
p1.printname()

#super.__init__ is used to pass value to the base class through inheritance
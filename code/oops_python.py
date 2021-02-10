#classes

# class a():
#     def __init__(self,fname,lname,salary):
#         self.fname=fname
#         self.lname=lname
#         self.salary=salary
#
#     def display(self):
#         #print("first name is : "+self.fname+" last name is : "+self.lname+" salary is :  "+int(self.salary+5000))
#         self.salary=int(self.salary+1000)
#         print(self.salary)
#
# obj=a("gaffar","shaikh",1000)
# obj2=a("khader","shaikh",3000)
#
# obj.display()
# obj2.display()

# for ob in(obj,obj2):
#     print(ob.fname,ob.lname,ob.salary)
#convert obj to dictionary
#print(obj.__dict__)


#inheritance



from abc import ABC ,abstractmethod

class computer(ABC):
    @abstractmethod
    def show(self):
        print("hello python!!!")


#to make a abtracrt class from abc imort ABC and abstractmethod


class laptop(computer):
    def show(self):
        print("hello python111")


ob1=laptop()
ob1.show()

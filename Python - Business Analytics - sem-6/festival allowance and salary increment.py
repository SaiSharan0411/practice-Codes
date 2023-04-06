# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 14:40:16 2023

@author: cat16
"""

print("20-uca-016")
print("Sai Sharan")

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
class employee(person):
    def __init__(self, name, age, empno, designation, department, salary):
        super().__init__(name, age)
        self.empno = empno
        self.designation = designation
        self.department = department
        self.salary = salary
        
    def myfunc(self):
        print("Hello my name is "+self.name)
        print("I am",self.age,"yeas old")
        print("my employee number",self.empno)
        print("my designation",self.designation)
        
    def increment(self,amount,event=None):
        if event is not None:
            print(event + "Allowance" + str(amount))
        else:
            print("old salary was:",str(self.salary))
            self.salary=self.salary+amount
            print("New Salary was: ",str(self.salary))
            
p1=employee(input("Enter a name: "),int(input("enter age: ")),int(input("Enter Employee No: ")),
            (input("Enter designation is: ")),(input("Enter Department is: ")),int(input("Enter Salary is: ")))
p1.myfunc()
p1.increment(50000)
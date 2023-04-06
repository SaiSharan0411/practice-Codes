# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 17:54:42 2023

@author: cat16
"""

print("20-uca-016")
print("sai")

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
class Employee(person):
    def __init__(self,name,age,empno,designation,department,salary):
        super().__init__(name,age)
        self.empno=empno
        self.desig=designation
        self.dept=department
        self.salary=salary
        
    def myfunc(self):
        print("Hello my name is " + self.name)
        print("I am ", self.age, "years old")
        print("My Employee number is ", self.desig)
        print("The department i work in is ",self.dept)
        print("My salary package is ", self.salary)
        
p1=Employee(input("Enter your name: "),int(input("Enter your age: ")),input("Enter your employee number: "),
            input("Enter your Designation: "),input("Enter your Department: "),int(input("Enter your salary: ")))
p1.myfunc()
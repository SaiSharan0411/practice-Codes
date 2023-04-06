# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 17:54:12 2023

@author: cat16
"""

print("20-uca-016")
print("sai")

class person:
    def __init__(self,name,age,gender,contactno):
        self.name=name
        self.age=age
        self.gender=gender
        self.contactno=contactno
        
    def myfunc(self):
        print("hello my name is "+self.name)
        print("I am ",self.age,"years old")
        print("I am a "+self.gender)
        print("My contact number is ",self.contactno,".")
        
p1=person(input("Enter your Name: "),int(input("Enter your age: ")),input("Enter your gender: "),int(input("Enter your contact number: ")))
p1.myfunc()
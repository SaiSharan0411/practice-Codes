# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 15:10:10 2023

@author: cat16
"""

print("20-uca-016")
print("Sai Sharan")

tax=0
income=int(input("Enter your income: "))
if(income>100000 and income<300000):
    tax=(income-100000)*0.1
    print("tax=10%")
elif(income>300000 and income<500000):
    tax=20000+(income-300000)*0.2
    print("tax=20%")
elif(income>500000):
    tax=20000+40000+(income-500000)*0.3
    print("tax=30%")
else:
    tax=0
print("Your tax amount is: ",tax)
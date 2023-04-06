# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 13:45:21 2023

@author: cat16
"""

print("20-uca-016")
print("Sai Sharan")

print("Currency conversion from inr to usd, yen, euro and sgd")

inr=int(input("Enter rupee amount :"))
res=lambda x:inr/x
print("in dollar :",res(82))
print("in yen :",res(12))
print("in euro :",res(89))
print("in sgd :",res(62))
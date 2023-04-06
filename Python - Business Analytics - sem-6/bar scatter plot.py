 # -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 13:55:09 2023

@author: cat16
"""

print("20-uca-016")
print("Sai Sharan")

import pandas as pd
data=pd.read_csv("TestData.csv")
print(data)
print(data.info())
print(data.describe())

data.plot.bar("Income","Expenses")
data.plot.scatter("Month","Income",10)
data.plot.scatter("Month","Expenses",10)
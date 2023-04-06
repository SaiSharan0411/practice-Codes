# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 14:47:41 2023

@author: cat16
"""

print("20-uca-016")
print("Sai Sharan")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data = pd.read_csv("TestData.csv")
plt.plot(data['Month'],data['Profit'],color='coral')
print(data['Month'][0])
plt.xlabel('Month')
plt.xticks(rotation=62)
plt.ylabel('Profit')
plt.title('Profit over a period of 21 months')
plt.show()
plt.plot(data['Month'],data['Income'],color='aqua')
plt.xlabel('Month')
plt.xticks(rotation=62)
plt.ylabel('Income')
plt.title('Income over a period of 21 months')
plt.show()
plt.plot(data['Month'],data['Expenses'],color='violet')
plt.xlabel('Month')
plt.xticks(rotation=62)
plt.ylabel('Expenses')
plt.title('Expenses over a period of 21 months')
plt.show()

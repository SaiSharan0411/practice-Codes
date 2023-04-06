# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 13:44:01 2023

@author: cat16
"""

print("20-uca-016")
print("Sai Sharan")

import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv("TestData.csv")
x=data.iloc[:,8].values.reshape(-1,1)
y=data["Profit"].values.reshape(-1,1)
plt.scatter(x,y)
plt.plot(x,y,color='red')
plt.show()
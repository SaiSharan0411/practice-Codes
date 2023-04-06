# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 14:47:59 2023

@author: cat16
"""

print("20-uca-016")
print("Sai Sharan")

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
data=pd.read_csv("Currencies.csv")
print(data)
print(data.info())
print(data.describe())
figure,axes=plt.subplots(nrows=3,ncols=2,figsize=(20,10))
data.plot(x='Year',y='USD',ax=axes[0,0],color='blue')
data.plot(x='Year',y='Yen',ax=axes[0,1],color='red')
data.plot(x='Year',y='Peso',ax=axes[1,0],color='green')
data.plot(x='Year',y='Ruble',ax=axes[1,1],color='orange')
data.plot(x='Year',y='SGD',ax=axes[2,0],color='purple')
data.plot(x='Year',y='EURO',ax=axes[2,1],color='yellow')
plt.tight_layout()
plt.show()

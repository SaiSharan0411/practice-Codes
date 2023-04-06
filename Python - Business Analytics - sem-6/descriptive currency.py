# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 14:03:21 2023

@author: cat16
"""

print("20-uca-016")
print("Sai Sharan")

import pandas as pd

x=[2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023]
x=pd.DataFrame(x)
print(x.describe())
print(x.info())

y1=[58.5,60.9,64.1,69,68,68.4,70.4,74.1,73.9,74.4,81.2]
y1=pd.DataFrame(y1)
print(y1.describe())
print(y1.info())

y2=[79.790,97.596,105.945,121.044,108.793,112.166,110.423,109.010,106.775,109.745,131.498]
y2=pd.DataFrame(y2)
print(y2.describe())
print(y2.info())

y3=[13.169,12.772,13.292,15.848,18.664,18.927,19.244,19.264,21.486,20.272,20.127]
y3=pd.DataFrame(y3)
print(y3.describe())
print(y3.info())

y4=[30.840,31.837,38.378,60.938,67.056,58.343,62.668,64.732,72.105,73.654,73.23]
y4=pd.DataFrame(y4)
print(y4.describe())
print(y4.info())

import matplotlib.pyplot as plt
plt.plot(x,y1,label="USD")
plt.plot(x,y2,label="YEN")
plt.plot(x,y3,label="PESO")
plt.plot(x,y4,label="RUBLE")

plt.xlabel("YEARS")
plt.xlabel("Average Exchange Rate")
plt.xlabel("Currency Exchange in Rate past 10 years")
plt.legend()
plt.show()
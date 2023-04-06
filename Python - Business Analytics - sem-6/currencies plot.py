# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 14:55:45 2023

@author: cat16
"""

print("20-uca-016")
print("Sai Sharan")

import pandas as pd
data=pd.read_csv("Currencies.csv")
print(data)
print(data.describe())
import matplotlib.pyplot as plt
plt.plot(data["Year"],data["USD"],label="USD")
plt.plot(data["Year"],data["Yen"],label="Yen")
plt.plot(data["Year"],data["Peso"],label="Mexican Peso")
plt.plot(data["Year"],data["Ruble"],label="Russian Ruble")
plt.plot(data["Year"],data["SGD"],label="Singapore Dollar")
plt.plot(data["Year"],data["EURO"],label="Euro")
plt.legend(loc='upper left')

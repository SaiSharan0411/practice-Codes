# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 13:41:35 2023

@author: cat16
"""

print("20-uca-016")
print("Sai Sharan")

import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv('attendance11.csv')

plt.plot(data['Attendance Date'],data['1'],color='red',label='first hour')
plt.plot(data['Attendance Date'],data['2'],color='blue',label='second hour')
plt.plot(data['Attendance Date'],data['3'],color='green',label='third hour')
plt.plot(data['Attendance Date'],data['4'],color='yellow',label='fourth hour')
plt.plot(data['Attendance Date'],data['5'],color='pink',label='fifth hour')
plt.xlabel("Date")
plt.ylabel("Attendance")
plt.title("Attendance for first hour")
plt.xticks(rotation=90)
plt.legend()
plt.show()

data=pd.read_csv('attendance11.csv')

figure,axes=plt.subplots(nrows=2,ncols=2,figsize=(20,10))
data.plot(x='Attendance Date',y="1",ax=axes[0,0],color="red")
data.plot(x='Attendance Date',y="2",ax=axes[0,1],color="blue")
data.plot(x='Attendance Date',y="3",ax=axes[1,0],color="green")
data.plot(x='Attendance Date',y="4",ax=axes[1,1],color="yellow")
plt.tight_layout()
plt.show()
plt.legend()
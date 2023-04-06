# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 13:39:55 2023

@author: cat16
"""

print("20-uca-016")
print("Sai Sharan")

import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("attendance.csv")
present=0
absent=0
od=0
ml=0
cl=0
dayOrder=[]
for i in data:
    dayOrder.append(i)
for index, row in data.iterrows():
    for day in dayOrder:
       if(day=='Attendance Date'):
           continue
       if(row[day]=='P'):
           present+=1
       elif(row[day]=='A'):
           absent+=1
       elif(row[day]=='OD'):
           od+=1
       elif(row[day]=='ML'):
           ml+=1
       elif(row[day]=='CL'):
           cl+=1
print("Day Order List: ",dayOrder)
print("No.of hours Present: ",present)
print("No.of hours Absent: ",absent)
print("No.of hours OD",od)
print("No.of hours ML",ml)
print("No.of hours CL",cl)
x=[present,absent]
labels=["Present","Absent"]
if(od!=0):
    x.append(od)
    labels.append("OD")
if(ml!=0):
    x.append(ml)
    labels.append("ML")
if(cl!=0):
    x.append(cl)
    labels.append("CL")
plt.pie(x,labels=labels,autopct='%1.1f%%')
plt.title("Attendance Chart")
plt.axis('equal')
    
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 18:08:55 2023

@author: cat16
"""

print("20-uca-016")
print("Sai Sharan")

for index in range(100):
    print(index)
    
num_days=[31,28,31,30,31,30,31,31,30,31,30,31]

months=["January","February","March","April","May","June","July","August","September","October","November","December"]
print("Calendar - 2023")

i=0
j=0

while(i<len(months)):
    print(months[i])
    for num_day in range(1,num_days[i]+1):
        print(num_day,end=" ")
        if(num_day%7==0):
            print("")
    print("\n")
    i=i+1
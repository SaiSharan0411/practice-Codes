# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 17:12:22 2023

@author: cat16
"""

print("20-uca-016")
print("Sai Sharan")

def findAge(name, current_date, current_month, current_year, birth_date, birth_month, birth_year):
    
    month=[31,28,31,30,31,30,31,31,30,31,30,31]
    if(birth_date>current_date):
        current_month=current_month-1
        current_date=current_date+month[birth_month-1]
        
    if(birth_month>current_month):
        current_year=current_year-1
        current_month=current_month+12
        
    calc_date=current_date-birth_date;
    calc_month=current_month-birth_month;
    calc_year=current_year-birth_year;
        
    print("\n",name, "Your present is calculated below")
    print("years:", calc_year, "\nMonths:", calc_month, "\nDays:", calc_date)
    
current_date=2
current_month=2
current_year=2023 
    
name="Sai Sharan"
birth_date=11
birth_month=4
birth_year=2002
    
findAge(name, current_date, current_month, current_year, birth_date, birth_month, birth_year)
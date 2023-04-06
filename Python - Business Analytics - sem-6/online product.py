# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 14:19:39 2023

@author: cat16
"""

print("20-uca-016")
print("Sai Sharan")

q=[]
x=-1
a=1
while(a==1):
    print("\n Online Cart Management")
    print("1.Add item to cart")
    print("2.Remove the new item from the cart")
    print("3.display")
    print("4.exit")
    ch=int(input("Enter the choice: "))
    if(ch==1):
        name=(input("Enter the Item name: "))
        x=x+1
        q.insert(x,name)
    elif(ch==2):
        y=q.pop()
        print("The item removed",y)
        x=x-1
    elif(ch==3):
        print("Stack: ",q)
    elif(ch==4):
        break
    else:
        print("Invalid Choice")
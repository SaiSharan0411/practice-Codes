# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 14:05:37 2023

@author: cat16
"""

print("20-uca-016")
print("Sai Sharan")

q=[]
x=1
a=1
while (a==1):
    print("BANKING QUEUE-YOUR CHOICE")
    print("1.OBTAIN")
    print("2.WHOSE TURN NOW")
    print("3.DISPLAY")
    print("4.EXIT")
    
    ch=int(input("Enter the choice: "))
    if(ch==1):
        name=(input("Enter the customer name: "))
        y=q.append(name)
        y1=q.append(x)
        x=x+1
    elif(ch==2):
        y=q.pop(0)
        y1=q.pop(0)
        print(y)
        print(y1)
    elif(ch==3):
        print("queue",q)
    elif(ch==4):
        print("GOOD BYE")
        break
    else:
        print("Invalid Choice")
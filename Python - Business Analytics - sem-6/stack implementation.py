# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 16:56:14 2023

@author: cat16
"""

print("20-uca-016")
print("Sai Sharan")

print("Stack Implementation")

s=[]
top=-1

print("\n Menu for stack operations\n")
print("1.Push")
print("2.Pop")
print("3.Display")
print("4.Exit")

ch=int(input("Enter the choice: "))

if(ch==1):
    top=top+1
    x=int(input("Enter the Number: "))
    s.insert(top,x)
    
    if(ch==2):
        y=s.pop()
        print("the popped element ",y)
        top=top-1
    if(ch==3):
        print("Stack: ",s)
    if(ch==4):
        exit()
else:
    print("Invalid Choice ")
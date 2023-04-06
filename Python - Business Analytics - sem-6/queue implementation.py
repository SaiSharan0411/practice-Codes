# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 17:56:03 2023

@author: cat16
"""

q=[]
a=1

while (a==1):
    print("Menu for Queue Operations")
    print("1.Insert")
    print("2.Delete")
    print("3.Display")
    print("4.Exit")
    
    ch=int(input("Enter the choice: "))

    if(ch==1):
        x=int(input("Enter the Number"))
        y=q.append(x)
    
    if(ch==2):
        y=q.pop()
        
    if(ch==3):
        print("Queue: ",q)
        
    if(ch==4):
        exit()
    else:
        print("Invalid Choice ")
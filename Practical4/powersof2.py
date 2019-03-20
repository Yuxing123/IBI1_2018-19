# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:41:42 2019

@author: 52935
"""

# start from 2**13 to 2**0
# use x-2**n judge the answer wether >= 0
# if >=0 record n

x=4562
y=str(x)+" is "
n=13
for i in range (0,14):
    if x-2**n>0:
        x=x-2**n
        y=y+"2**"+str(n)+" + "
    elif x-2**n==0:
        x=0
        y=y+"2**"+str(n)
    else:
        x=x
        y=y
    n=n-1
print(y)
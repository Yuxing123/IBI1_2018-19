# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:00:59 2019

@author: 52935
"""

L = input("give me a string of words :")
L = L[::-1]
L = L.split(" ")
L.sort(reverse=True)
print(L)

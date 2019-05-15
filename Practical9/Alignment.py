# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 09:28:22 2019

@author: 52935
"""
import pandas as pd
s = open(r'C:\Users\52935\Desktop\ibi\IBI1_2018-19\Practical9/seq1.txt')
t = open(r'C:\Users\52935\Desktop\ibi\IBI1_2018-19\Practical9/seq2.txt')
k = open(r'C:\Users\52935\Desktop\ibi\IBI1_2018-19\Practical9/seq3.txt')
seq1 = s.read()
seq2 = t.read()
seq3 = k.read()
#input the sequence
data= pd.read_csv(r'C:\Users\52935\Desktop\ibi\IBI1_2018-19\Practical9/matrix.txt',sep=r' +',engine='python')
#imput the matrix 
blosum= data.to_dict()
count = 0
i = 0

for k in seq1:
    try:
        count = count + blosum[k][seq2[i]]
        i=i+1
    except:
        count=count
        i=i+1

print(count)
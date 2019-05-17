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
identical1=0
identical2=0
identical3=0
count1 = 0
count2 = 0
count3 = 0
i = 0
p = 0
q = 0
finalseq1=''
finalseq2=''

for a in seq1:
    try:
        count1 = count1 + blosum[a][seq2[i]]
        finalseq1 = finalseq1 + a
        finalseq2 = finalseq2 + seq2[i]
        if a==seq2[i]:
            identical1+=1
            finalseq1 += '+'
            finalseq2 += '+'
        else:
            identical1=identical1
            finalseq1=finalseq1
            finalseq2=finalseq2#make graph
        i=i+1
    except:
        count1=count1
        i=i+1
percentage1=identical1/len(seq1)
print('BLOSUM score for mouse human comparison:',count1)
print('identity  for mouse human comparison is %.1f%%'%(percentage1*100))
# mouse human comparision

for b in seq1:
    try:
        count2 = count2 + blosum[b][seq3[p]]
        if b==seq3[p]:
            identical2+=1
        else:
            identical2=identical2
        p=p+1
    except:
        count2=count2
        p=p+1
percentage2=identical2/len(seq1)
print('BLOSUM score for human random seq comparison',count2)
print('identity  for human random seq comparison is %.1f%%'%(percentage2*100))
# human random seq comparison
for c in seq2:
    try:
        count3 = count3 + blosum[c][seq3[q]]
        if c==seq3[q]:
            identical3+=1
        else:
            identical3=identical3
        q=q+1
    except:
        count3=count3
        q=q+1
percentage3=identical3/len(seq2)
print('BLOSUM score for mouse random seq comparison:',count3)
print('identity  for mouse random seq comparison is %.1f%%'%(percentage3*100))

print('visual Aliment is:','\n',finalseq1,'\n',finalseq2)
#mouse random seq comparison

f=open(r'C:\Users\52935\Desktop\ibi\IBI1_2018-19\Practical9/summary.txt','w')
f.write('BLOSUM score for mouse human comparison:'+str(count1)+'\n')
f.write('identity  for mouse human comparison is %.1f%%'%(percentage1*100)+'\n')
f.write('BLOSUM score for human random seq comparison'+str(count2)+'\n')
f.write('identity  for human random seq comparison is %.1f%%'%(percentage2*100)+'\n')
f.write('BLOSUM score for mouse random seq comparison:'+str(count3)+'\n')
f.write('identity  for mouse random seq comparison is %.1f%%'%(percentage3*100)+'\n')
f.close()
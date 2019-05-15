# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:34:03 2019

@author: Lenovo
"""
# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
n=0
while n<=1:
    p = 10000 
    v=int(p*n)
    ps = int(10000-v)
    pi = 1
    pr = 0
#p = population ps = population susceptible pi = population infected pr = population recovered v=

    beta = 0.3
    gamma = 0.05
#beta = infection probability  gamma = recovery probability
    psset=[ps]
    piset=[1]
    prset=[0]
    count=0

    while count<=1000:
        count+=1
        Newinfected=sum(np.random.choice(range(2),ps,p=[1-beta*pi/p,beta*pi/p]))
        Newrecovered=sum(np.random.choice(range(2),pi,p=[1-gamma,gamma]))
        pi=pi+Newinfected-Newrecovered
        ps=ps-Newinfected
        pr=pr+Newrecovered
        psset.append(ps)
        piset.append(pi)
        prset.append(pr)
    plt.plot(piset,label=str(n))
    plt.xlabel('time')
    plt.ylabel('number of people')
    plt.legend()
    plt.title('SIR model with different vaccination rates')
    n=round(n+0.1,1)

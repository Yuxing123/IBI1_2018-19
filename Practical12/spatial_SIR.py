# -*- coding: utf-8 -*-
"""
Created on Wed May  8 16:26:05 2019

@author: Lenovo
"""

# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
#function to judge if the person is infected
def infection(x,y):
    if x>=100 or x<=-1 or y>=100 or y<=-1:
        pass
    else:
        if population[x,y]==1 or population[x,y]==2:
            pass
        else:
            rate = np.random.choice(range(2),1,p=[1-beta,beta])
            population[x,y]=rate[0]
# make array of all susceptible population
population = np.zeros((100,100))
outbreak = np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]] = 1
beta = 0.3
gamma = 0.05

n=0
while n<= 100:
    if n == 0 or n == 10 or n == 50 or n == 100:
        plt.figure(figsize=(6,4),dpi =150)
        plt.imshow(population,cmap='viridis',interpolation='nearest')
    else:
        pass
    infected = np.where(population==1)
    for i in range(0,len(infected[0])):    #search for all infected people
        infection(infected[0][i]-1,infected[1][i]-1)
        infection(infected[0][i]-1,infected[1][i])
        infection(infected[0][i]-1,infected[1][i]+1)
        infection(infected[0][i],infected[1][i]-1)
        infection(infected[0][i],infected[1][i]+1)
        infection(infected[0][i]+1,infected[1][i]-1)
        infection(infected[0][i]+1,infected[1][i])
        infection(infected[0][i]+1,infected[1][i]+1)
        recoverrate = np.random.choice((1,2),1,p=[1-gamma,gamma])
        population[infected[0][i],infected[1][i]]=recoverrate[0]
    n=n+1

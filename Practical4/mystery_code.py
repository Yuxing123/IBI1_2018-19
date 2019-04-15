# What does this piece of code do?
# Answer: 
#Find a random prime number in range (1,100) 
#The code randomly choose a number between 1 and 100 and test this number if it can be divided by 2 to the square root of it.
# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

p=False
while p==False:
    p=True
    n = randint(1,100)
    u = ceil(n**(0.5))
    for i in range(2,u+1):
        if n%i == 0:
            p=False
            

     
print(n)

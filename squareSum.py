# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 19:04:41 2021

@author: avina
"""

n = int(input('Enter the number '))

i = 1
sum = 0;

while i <= n :
    sum += (i**2)
    i+=1

print(sum)


import random

rand = random.randint(0, 10)
print(rand)
num = -1

while num != rand :
    num = int(input ('Enter a number between 0 and 10 '))
    
print('Well Done!')

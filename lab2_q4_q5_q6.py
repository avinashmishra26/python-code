# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 18:43:06 2021

@author: avina
"""

n = int(input('Enter the number '))
print(sum(range(3,n+1)))

print(sum(range(3,n+1,2)))

print(sum(range(3,n+1,3)))


for num in range(n,-1,-1):
    print(num)
    
#Factorial
mul = 1
for num in range(1,n+1):
    mul*=num

print(mul)
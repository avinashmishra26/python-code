# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 18:40:58 2021

@author: avina
"""

n = int(input('Enter the number '))
sum =0
for num in range(3,n+1):
    if num % 3 == 0:
        sum += num
    
print(sum)
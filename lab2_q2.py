# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 18:40:00 2021

@author: avina
"""



n = int(input('Enter the number '))
sum =0
for num in range(3,n+1):
    if num % 2 == 1:
        sum += num
    
print(sum)



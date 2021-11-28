# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 18:50:06 2021

@author: avina
"""

n = input('Enter the number ')

if n.lstrip('-').isdigit():
    n = int(n)
    if n > 0 :
        print('{} is positive'.format(n))
    elif n < 0 :
        print('{} is negative'.format(n))
    else :
        print('{} is Zero'.format(n))
else:
    print('string is not a number')


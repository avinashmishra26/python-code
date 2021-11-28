# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 15:33:46 2021

@author: avina
"""

s = "Hello There"

s1 = list(s)

print(s1)

s2 = s.split()

print(s2)


print("writng   ",''.join(s1))

l = [9,6,0,3]

l1 = sorted(l)
 
print(l1)

l.sort()

print(l)


l.reverse()
print(l)


warm = ['red','yellow','green']

hot = warm

hot.append('pink')

print(hot)


import math

def decompose(x):
    return (math.cos(x),math.sin(x))

decompose(0)
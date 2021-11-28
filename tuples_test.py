# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 14:45:39 2021

@author: avina
"""

t = (1, "avi", "machine learning")
print(t)

print(id(t))

t = t + (5,6)
print(t)
print(id(t))


print(t[2])

#t[2] = "sds"  ERROR

x = 2
y = 3

(x,y) = (y,x)

print(x,y)


def always_sunny(t1, t2):

    sun = ("sunny","sun")    
    print(t1[0])    
    print(t2[0])

    first = t1[0] + t2[0]
    return (sun[0], first)


print(always_sunny(('cloudy'), ('cold',)))

temp = ('avinash')
print(temp[0])

temp1 = ('avinash',)
print(temp1[0])

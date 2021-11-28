# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

local is any combination of alphanumeric (i.e., both letters and numbers) 
charcters in either lower or upper case, dots (.) and the following 
characters !#$%&'*+-/=?^_`{|}~ , and
"""

mapVa = map(lambda x, y: x if x<y else y, [1,2,3,4],[0,9,2,5])

for i in mapVa:
    print(i)

def factR(n):
    if n == 1:
        return 1
    else :
        return n*factR(n-1)

def applyToEach(L, f):
    """ Assumes L is a list, f a function 
        Mutates L by replacing each element, e, of L by f(e)"""
        
    for i in range(len(L)):
        L[i] = f(L[i])
            
            
            
L = [1, -2, 3.33]
applyToEach(L, abs)
print('Apply abs to each element of L::',L)

applyToEach(L, int)
print('Apply int to each element of L::',L)


applyToEach(L, factR)
print('Apply factorial to each element of L::',L)
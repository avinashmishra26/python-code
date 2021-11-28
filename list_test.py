# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 15:04:31 2021

@author: avina
"""

L = [2, "avi", "CS", [2,3]]
print(L)

print(L[2])

print(L[3])

#list is mutuable


L = [2,5,3]

total = 0
for i in range(len(L)):
    total += L[i]
print(total)


#efficient Way is below

total1 = 0
for ele in L:
    total1 += ele
print(total1)

L.append(100)
print(L)


L1 = [2,1,3]
L2 = [4,5,6]

L3 = L1+L2
print(L3)

L1.extend([100, 200 ])


print(L1)

l_str = ['a','bc','def']

print(''.join(l_str))


print('_'.join(l_str))


print(' avi '.join(l_str))



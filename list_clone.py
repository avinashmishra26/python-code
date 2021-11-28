# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 15:53:31 2021

@author: avina
"""

cool = ['blue','green','grey']

warm = cool[:]
warm.append('black')
print(warm)

just_few = cool[:1]

print(just_few)


num1 = [2,3,1,4]
num2 = [5,6,1,2]
loop_counter = 0

for e1 in num1[:]:
    loop_counter+=1
    if e1 in num2:
        num1.remove(e1)

print(num1,loop_counter)


L1 = ['re']
L2 = ['mi']
L3 = ['do']

L4 = L1 + L2

L3.extend(L4)
L3.sort()

del(L3[0])

L3.append(['fa','la'])

print(L3)
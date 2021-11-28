# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 16:36:17 2021

@author: avina
"""

L1 = ["bacon", "eggs"]
L2 = ["toast", "jam"]

brunch = L1

L1.append("juice")

brunch.extend(L2)

print(brunch)


def builder(L1, L2, s):
    temp = L1[:]
    temp.append(s)
    temp.extend(L2)
    return temp
    
    
    
print(builder( ["bacon", "eggs"], ["toast", "jam"],"juice"))
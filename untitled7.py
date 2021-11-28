#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 00:57:29 2021

@author: avinashkumarmishra
"""

def foo(codeList, shoppingCart):
    index = 0
    for each_group in codeList:
        #print(index)
        index = find_last_index(each_group, shoppingCart[index:])
        if index == -1:
            return 0
    return 1
        
def find_last_index(each_group, shoppingCart):
    for idx in range(len(shoppingCart)):
        i = 0
        if shoppingCart[idx] == each_group[i] or each_group[i] == 'anything':
            j, i = idx+1 , i+1
            while j<len(shoppingCart) and i<len(each_group) and (shoppingCart[j] ==  each_group[i] or each_group[i] == 'anything'):
                j, i = j+1 , i+1
            if (i-1) == (len(each_group) -1):
                return j
    return -1


codeList = [['orange'],['apple','apple'],['banana','orange','apple'],['banana']]

shoppingCart = ['orange','apple','apple','banana','orange','apple','banana']

print(foo(codeList, shoppingCart))
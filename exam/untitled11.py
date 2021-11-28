#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 22:43:08 2021

@author: avinashkumarmishra
"""


def recur_test(a):
    print(id(a))
    
    if len(a) == 1:
        return
    
    recur_test(a[0:1])
    
    
a= [1,2,3] 
print(id(a))   
recur_test(a)
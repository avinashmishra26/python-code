#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 00:14:25 2021

@author: avinashkumarmishra
"""



def max_gold(arr):
    if len(arr) == 1:
        return arr[0]
    
    
    if len(arr) >=3 :
        max_first = max_gold(arr[2:])
    else:
        max_first = 0
        
    max_first = arr[0]+max_first
    
    if len(arr) >=4 :
        max_second = max_gold(arr[3:])
    else:
        max_second = 0
        
    max_second = arr[1]+max_second
    
    if max_first > max_second:
        return max_first
    else :
        return max_second
    
    
    
max_gold([5,4,3,7,4,2])
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 12:35:23 2021

@author: avinashkumarmishra
"""

def trap_water(arr):
    
    max_water = 0.0
    index = None
    
    for idx1 in range(len(arr)-1):
        for idx2 in range(idx1+1,len(arr)):
            if min(arr[idx1] , arr[idx2]) * (idx2-idx1) > max_water:
                max_water = min(arr[idx1] , arr[idx2]) * (idx2-idx1)
                index=((idx1,idx2),)
                
                
                
    print(max_water, index)
    
def get_max_trapped_water(heights) :
    
    i, j = 0 , len(heights) - 1
    max_water , index = 0 , None
    
    while i < j:
        w = (j-i) * min (heights[i], heights[j])
        if w > max_water:
            max_water = w
            index = ((i,j),)
            
        if heights[i] > heights[j]:
            j -= 1
        else :
            i += 1
    print(max_water, index)
   
   
trap_water([1,2,1,3,4,4,5,6,2,1,3,1,3,2,1,2,4,1])
            
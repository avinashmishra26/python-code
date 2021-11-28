#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 22:00:08 2021

@author: avinashkumarmishra
"""

def merge_sort(arr, start, end):
    
    if start < end:
        middle = (start + end) // 2 
        merge_sort(arr, start, middle)
        merge_sort(arr, middle+1, end)
        merge(arr, start, middle, end)
        
        
def merge(arr, start, mid, end):
    print(arr, start, mid, end)
    lstart = start
    lend = mid
    rstart = mid + 1
    rend = end
    
    temp = []
    
    while lstart <= lend and rstart <= rend:
        if arr[lstart] < arr[rstart]:
            temp.append(arr[lstart])
            lstart += 1
        else:
            temp.append(arr[rstart])
            rstart += 1
        
    while lstart <= lend:
        temp.append(arr[lstart])
        lstart += 1
            
    while rstart <= rend:
        temp.append(arr[rstart])
        rstart += 1
    
    i = start
    for ele in temp:
        arr[i] = ele
        i += 1
        
  
a = [4,3,2,1]
merge_sort(a, 0, 3)
    
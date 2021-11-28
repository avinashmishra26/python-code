#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 10:36:50 2021

@author: avinashkumarmishra
"""

def number_of_ways_to_top(n, k):
    
   
    def  ways_to_top_helper(n, k):
       if not n:
           count.append(1)
           return

        
       for i in range(1, k+1):
           if len(n[:i]) == i:
               ways_to_top_helper(n[i:], k)
      
    count = []
    ways_to_top_helper(n, k)
    return len(count)
    

print(number_of_ways_to_top([1,2,3,4], 2))
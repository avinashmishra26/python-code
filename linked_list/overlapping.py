#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 15:26:56 2021

@author: avinashkumarmishra
"""

def overlapping_no_cycle_lists(L1, L2):
    
    def list_length(L):
        step = 0
        while L:
            step += 1
            L = L.next
        return step
    
    
    len_l1, len_l2 = list_length(L1) , list_length(L2)
    
    if len_l1 < len_l2:
        L1, L2 = L2, L1
        
    
    for _ in range(abs(len_l2-len_l1)):
        L1= L1.next
        
        
    for _ in range(min(len_l1, len_l2)):
        if L1 == L2:
            return L1
        L1, L2 = L1.next, L2.next      
    return None        
    
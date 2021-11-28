#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 17:33:19 2021

@author: avinashkumarmishra
"""

def reverse_sublist(L , node_no1, node_n02):
    i = 1
    
    s_prev = p = q = r = None
    
    while L and i < node_no1:
        s_prev = L
        L = L.next
        i += 1
    
    p = L
    q = L.next
    r = L.next.next     
    while i < node_n02 and q:
         q.next = p
         i +=1
         p = q
         q = r
         r = r.next
    
    s_prev.next.next = q     
    s_prev.next = p
     
    
    
               
        
    
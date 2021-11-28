#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 12:16:55 2021

@author: avinashkumarmishra
"""

def has_cycle(head):
    
    p = q = head
    
    while q and q.next and q.next.next:
        if p == q:
            print('It has a cycle')
        p = p.next
        q = q.next.next
        cycle_l = cycle_len(p)
        
        cycle_iter = head
        for _ in range(len(cycle_l)):
            cycle_iter = cycle_iter.next
            
        h_0 = head
        
        while h_0 != cycle_iter:
            h_0 = h_0.next
            cycle_iter = cycle_iter.next
        return h_0
        
    return None
        
        
        
        
def cycle_len(p_node):
    start = p_node
    steps = 0
    
    while True:
        steps += 1
        start = start.next
        if start == p_node:
            return steps
    
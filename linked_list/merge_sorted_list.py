#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 16:35:02 2021

@author: avinashkumarmishra
"""

from listNode import ListNode

def sort_list(L1, L2):
    
    dummy_head = tail = ListNode()
    
    while L1 and L2:
        if L1.data < L2.data:
            tail.next = L1
            L1 = L1.next
        else:
            tail.next = L2
            L2 = L2.next
        tail = tail.next
    
    tail.next = L1 or L2    
    return dummy_head.next
        
    
    
            
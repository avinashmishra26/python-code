#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 16:07:10 2021

@author: avinashkumarmishra
"""

class ListNode:
    
    def __init__(self, data = 0, next_node = None):
        self.data = data
        self.next = next_node
        
        
        
        
def search(L, key):
    while L and L.data != key:
            L = l.next        
    return L 

def insert_after(node, new_node):
    new_node.next = node.next
    node.next = new_node
    
    
def delete_after(node):
    node.next = node.next.next
    
    
        
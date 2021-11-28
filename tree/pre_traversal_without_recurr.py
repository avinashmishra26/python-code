#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 21:06:29 2021

@author: avinashkumarmishra
"""

from tree_helper import pre_order_traversal, initialize_binary_tree_LCA

def pre_traversal_without_recurr(tree):
    
    result = []
    stck = []
    
    while tree or stck:
        
        if tree:
            result.append(tree.data)
            stck.append(tree)
            tree = tree.left
            
        else:
            el = stck.pop()
            tree = el.right
    
    return result
    
    
    
print(pre_order_traversal(initialize_binary_tree_LCA()))        
print(pre_traversal_without_recurr(initialize_binary_tree_LCA()))
    
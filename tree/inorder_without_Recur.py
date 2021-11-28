#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 15:24:56 2021

@author: avinashkumarmishra
"""

from tree_helper import in_order_traversal, initialize_binary_tree_LCA

def  inorder_traversal_without_recurr(tree):
    
    stck = []
    result = []
    
    while tree or stck:
        
        if tree:
            stck.append(tree)
            tree = tree.left
            
        else:
            el = stck.pop()
            result.append(el.data)
            tree = el.right
        
    return result

print(in_order_traversal(initialize_binary_tree_LCA()))        
print(inorder_traversal_without_recurr(initialize_binary_tree_LCA()))


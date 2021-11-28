#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 21:18:50 2021

@author: avinashkumarmishra
"""

from tree_helper_bst import initialize_BST

def is_binary_tree_bst(tree, low_range = float('-inf'), high_range = float('inf')):
    
    if not tree:
        return True
    
    elif not low_range <= tree.data <= high_range:
        return False
    
    return (is_binary_tree_bst(tree.left, low_range, tree.data)  and \
           is_binary_tree_bst(tree.right, tree.data, high_range))
    
    
    
    
    
    
print(is_binary_tree_bst(initialize_BST()))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 18:05:25 2021

@author: avinashkumarmishra
"""

from tree_helper import initialize_binary_tree_root_to_leaf

def root_to_leaf_path(root):
    
    def root_leaf_helper(root):
        if not root.left and not root.right:
            return [str(root.data)]
        
        if not root.left:
            r_l = []
        else:
            r_l = root_to_leaf_path(root.left)
        if not root.right:
            r_r = []
        else:
            r_r = root_to_leaf_path(root.right)
    
    
        return list(map(lambda x: str(root.data)+x, r_l+r_r))
        
    return root_leaf_helper(root)   
        
        
print(root_to_leaf_path(initialize_binary_tree_root_to_leaf()))
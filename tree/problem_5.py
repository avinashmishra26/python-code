#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 00:48:29 2021

@author: avinashkumarmishra
"""

#incomplete

def sum_root_to_leaf(root):
    
    if not root:
        return 0
    
    
    return root.left + root.right
    
    
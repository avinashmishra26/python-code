#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 00:40:05 2021

@author: avinashkumarmishra
"""

from binaryTree import BinaryTreeNode
from tree_helper import initialize_binary_tree, initialize_symmtetric_binary_tree




def check_symmetric(left_subtree, right_subtree):
    
    
    if not left_subtree and not right_subtree:
        return True
    elif left_subtree == None or right_subtree == None or \
        left_subtree.data != right_subtree.data :
        return False
    
    
    
    if(not check_symmetric(left_subtree.left , right_subtree.right)):
        return False
    
    
    if(not check_symmetric(left_subtree.right , right_subtree.left)):
        return False
    
    return True
    
    
    
    
root = initialize_binary_tree()
print(check_symmetric (root.left, root.right))


root = initialize_symmtetric_binary_tree()
print(check_symmetric (root.left, root.right))
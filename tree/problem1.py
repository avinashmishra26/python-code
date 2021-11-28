#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 15 21:23:49 2021

@author: avinash
"""

from tree_helper import initialize_binary_tree

from collections import namedtuple

list_ = []

def  is_balanced_binary_tree(root):
    
    BalancedStatusWithHeight = namedtuple('BalancedStatusWithHeight',\
                                          ('balanced','height','node_value'))
        
    def check_balanced(root):
        
        if not root:
            return BalancedStatusWithHeight(True, -1,None)

    
        left_subtree = check_balanced(root.left)
        right_subtree = check_balanced(root.right)
        
        
        if not left_subtree.balanced:
             return BalancedStatusWithHeight(False, 0, left_subtree.node_value)
         
        if not right_subtree.balanced:
             return BalancedStatusWithHeight(False, 0, right_subtree.node_value)
        
        if left_subtree.balanced and right_subtree.balanced:
            left_height = left_subtree.height + 1
            right_height = right_subtree.height + 1
            height = left_height \
                        if left_height > right_height \
                        else right_height
            if abs(left_height - right_height) <= 2:
                return BalancedStatusWithHeight(True, height, root.data)
            else:
                return BalancedStatusWithHeight(False, height, root.data)

         
    return check_balanced(root)
            


    
root = initialize_binary_tree()
print(is_balanced_binary_tree(root).balanced)
print(is_balanced_binary_tree(root).node_value)

#post_order_traversal(root)
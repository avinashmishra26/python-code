#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 23:27:17 2021

@author: avinashkumarmishra
"""

from collections import namedtuple
from tree_helper import initialize_binary_tree

def lca(node, m, n):
    
    lcaNode = namedtuple('lcaNode',('node', 'no_of_elements_found'))
    
    def lca_helper(node):
        
        if not node:
            return lcaNode(None, 0)
        
        if node:
            lcaNode_l = lca_helper(node.left)
            if lcaNode_l.no_of_elements_found == 2:
                return lcaNode(min_for(lcaNode_l.node, node), 2) 

            lcaNode_r = lca_helper(node.right)
            if lcaNode_r.no_of_elements_found == 2:
                return lcaNode(min_for(lcaNode_r.node, node), 2) 
        
        if node.data == m or node.data == n:
            temp = 1
            if lcaNode_l.no_of_elements_found == 1 or lcaNode_r.no_of_elements_found == 1:
                temp += 1
            return lcaNode(node, temp)
                
        
        if lcaNode_l.no_of_elements_found == 1 and lcaNode_r.no_of_elements_found == 1:
            return lcaNode(node, 2)
        else:
            return lcaNode(node, lcaNode_l.no_of_elements_found+lcaNode_r.no_of_elements_found)
            
     
    def min_for(node1, node2):
        if not node1 or not node2:
            print('hi',node1, node2.data)
        if node1.data < node2.data:
            return node1
        else :
            return node2
        
    return lca_helper(node)   


res_node  = lca(initialize_binary_tree(), 641, 257)
print(res_node.node)
if res_node.node:
    print(res_node.node.data)
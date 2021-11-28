#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 03:36:56 2021

@author: avinashkumarmishra
"""

#brute Force
from collections import namedtuple
from tree_helper import initialize_binary_tree_LCA


def LCA_brute_force(root, m_data, n_data):
    lcas = namedtuple('lcas',('element_root','bal'))

    lst = []
    def find_LCA_root(root, m_data, n_data):
        
        if root.data == m_data and (check_node(root.left, n_data) \
            or check_node(root.right, n_data)):
            lst.append(lcas(root.data, True))
            print(1)
            
        elif root.data == n_data and (check_node(root.left, m_data) \
            or check_node(root.right, m_data)):
            lst.append(lcas(root.data, True))
            print(2)
            
            
        if check_node(root.left, m_data) and check_node(root.left, n_data):
            lst.append(lcas(root.data, True))
            find_LCA_root(root.left, m_data, n_data)
            print(3)
        elif check_node(root.right, m_data) and check_node(root.right, n_data):
            lst.append(lcas(root.data, True))
            find_LCA_root(root.right, m_data, n_data)
            print(4)
        elif (check_node(root.left, m_data) and check_node(root.right, n_data)) \
             or (check_node(root.right, m_data) and check_node(root.left, n_data)): 
            lst.append(lcas(root.data, True))
            print(5)
        
        
    
    def check_node(subtree , data):
        if subtree:
            if subtree.data == data:
                return True
            if check_node(subtree.left, data):
                return True
            if check_node(subtree.right, data):
                return True
            
            
    find_LCA_root(root, m_data, n_data) 
    return lst       
            

#res  = LCA_brute_force(initialize_binary_tree_LCA(), 'M', 'N')
#print(res[-1].element_root)



def find_lca(tree, node0, node1):
    pass 
    # TO DO
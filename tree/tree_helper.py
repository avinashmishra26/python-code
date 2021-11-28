#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 17:23:47 2021

@author: avinash
"""

from binaryTree import BinaryTreeNode

def pre_order_traversal(root):
    if root:
        print(root.data)
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)
        
        
def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.data)
        in_order_traversal(root.right)
        
        
        
def post_order_traversal(root):
    if root:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.data)
        
        
        
def initialize_binary_tree():
    root = BinaryTreeNode(314)
    root.left = BinaryTreeNode(6)
    root.right = BinaryTreeNode(16)
        
        
    root.left.left = BinaryTreeNode(271)
    root.left.right = BinaryTreeNode(561)
        
    root.right.left = BinaryTreeNode(2)
    root.right.right = BinaryTreeNode(271)
    
    
    root.left.left.left = BinaryTreeNode(28)
    root.left.left.right = BinaryTreeNode(0)
    

    root.left.right.right = BinaryTreeNode(3)
    
    root.left.right.right.left = BinaryTreeNode(17)
        
    root.right.left = BinaryTreeNode(2)
    root.right.right = BinaryTreeNode(271)
    
    
    root.right.left.right = BinaryTreeNode(1)
    root.right.right.right = BinaryTreeNode(28)
    
    
    root.right.left.right.left = BinaryTreeNode(401)
    root.right.left.right.right = BinaryTreeNode(257)
    
    root.right.left.right.left.right = BinaryTreeNode(641)
        
    return root



def initialize_symmtetric_binary_tree():
    root = BinaryTreeNode(314)
    root.left = BinaryTreeNode(6)
    root.right = BinaryTreeNode(6)
        
        
    root.left.right = BinaryTreeNode(2)
    root.right.left = BinaryTreeNode(2)
        
    root.left.right.right = BinaryTreeNode(3)
    root.right.left.left = BinaryTreeNode(3)
    

    
    return root




def initialize_binary_tree_LCA():
    root = BinaryTreeNode('A')
    root.left = BinaryTreeNode('B')
    root.right = BinaryTreeNode('I')
        
        
    root.left.left = BinaryTreeNode('C')
    root.left.right = BinaryTreeNode('F')
        
    root.right.left = BinaryTreeNode('J')
    root.right.right = BinaryTreeNode('O')
    
    
    root.left.left.left = BinaryTreeNode('D')
    root.left.left.right = BinaryTreeNode('E')
    

    root.left.right.right = BinaryTreeNode('G')
    
    root.left.right.right.left = BinaryTreeNode('H')
        
    
    
    root.right.left.right = BinaryTreeNode('K')
    root.right.right.right = BinaryTreeNode('P')
    
    
    root.right.left.right.left = BinaryTreeNode('L')
    root.right.left.right.right = BinaryTreeNode('N')
    
    root.right.left.right.left.right = BinaryTreeNode('M')
        
    return root


def initialize_binary_tree_root_to_leaf():
    root = BinaryTreeNode(1)
    
    root.left = BinaryTreeNode(0)
    root.right = BinaryTreeNode(1)
    
    root.left.left = BinaryTreeNode(0)
    root.left.right = BinaryTreeNode(1)
    
    root.right.left = BinaryTreeNode(0)
    root.right.right = BinaryTreeNode(0)
    
    root.left.left.left = BinaryTreeNode(0)
    root.left.left.right = BinaryTreeNode(1)
    
    root.left.right.right = BinaryTreeNode(1)
    
    root.left.right.right.left = BinaryTreeNode(0)
    
    
    root.right.left.right = BinaryTreeNode(0)
    root.right.right.right = BinaryTreeNode(0)
    
    
    root.right.left.right.left = BinaryTreeNode(1)
    root.right.left.right.right = BinaryTreeNode(0)
    
    root.right.left.right.left.right = BinaryTreeNode(1)
    
    return root



def initialize_BST():
    root = BinaryTreeNode(314)
    root.left = BinaryTreeNode(6)
    root.right = BinaryTreeNode(16)
        
        
    root.left.left = BinaryTreeNode(271)
    root.left.right = BinaryTreeNode(561)
        
    root.right.left = BinaryTreeNode(2)
    root.right.right = BinaryTreeNode(271)
    
    
    root.left.left.left = BinaryTreeNode(28)
    root.left.left.right = BinaryTreeNode(0)
    

    root.left.right.right = BinaryTreeNode(3)
    
    root.left.right.right.left = BinaryTreeNode(17)
        
    root.right.left = BinaryTreeNode(2)
    root.right.right = BinaryTreeNode(271)
    
    
    root.right.left.right = BinaryTreeNode(1)
    root.right.right.right = BinaryTreeNode(28)
    
    
    root.right.left.right.left = BinaryTreeNode(401)
    root.right.left.right.right = BinaryTreeNode(257)
    
    root.right.left.right.left.right = BinaryTreeNode(641)
    
    return root
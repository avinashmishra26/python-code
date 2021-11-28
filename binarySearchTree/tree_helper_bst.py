#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 17:23:47 2021

@author: avinash
"""

from binaryTree_bst import BinaryTreeNode

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
        
        


def initialize_BST():
    root = BinaryTreeNode(19)
    root.left = BinaryTreeNode(7)
    root.right = BinaryTreeNode(43)
        
        
    root.left.left = BinaryTreeNode(3)
    root.left.right = BinaryTreeNode(11)
        
    root.right.left = BinaryTreeNode(23)
    root.right.right = BinaryTreeNode(47)
    
    
    root.left.left.left = BinaryTreeNode(2)
    root.left.left.right = BinaryTreeNode(5)
    

    root.left.right.right = BinaryTreeNode(17)
    
    root.left.right.right.left = BinaryTreeNode(13)
        
    
    root.right.left.right = BinaryTreeNode(37)
    root.right.right.right = BinaryTreeNode(53)
    
    
    root.right.left.right.left = BinaryTreeNode(29)
    root.right.left.right.right = BinaryTreeNode(41)
    
    root.right.left.right.left.right = BinaryTreeNode(31)
    
    return root
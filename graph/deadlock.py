#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 13:42:21 2021

@author: avinashkumarmishra
"""

class GraphVertex:
    
    white, gray, black = range(3)
    
    def __init__(self):
        self.color = GraphVertex.white
        self.edges = []
        
        
def is_deadlocked(G):
    
    def has_cycle(vertex):
        
        
        if vertex.color == GraphVertex.gray:
            return True
        
        vertex.color = GraphVertex.gray
        
        if any(map(has_cycle, vertex.edges)):
            return True
        
        vertex.color = GraphVertex.black
        
        return False            
        
    if any(map(has_cycle , [v for v in G])):
        return True
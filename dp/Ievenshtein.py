#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 01:40:45 2021

@author: avinashkumarmishra
"""

#Compute the Levenshtein distance

import math

def levenshtein_distance(a, b):
    
    a_len = len(a)
    b_len = len(b)
    
    if len(a) == len(b) and len(a) == 0:
        return 0
    elif len(a) == 0 or len(b) == 0:
        return math.inf
        
    
    if a[a_len-1] != b[b_len-1]:
        return 1 +\
            min(levenshtein_distance(a[0:a_len-2], b[0:b_len-2]),\
                levenshtein_distance(a[0:a_len-1], b[0:b_len-2]),\
                levenshtein_distance(a[0:a_len-2], b[0:b_len-1]))
    else :
        return levenshtein_distance(a[0:a_len-2], b[0:b_len-2])
    
    

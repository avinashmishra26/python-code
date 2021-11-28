#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 17:24:03 2021

@author: avinashkumarmishra
"""

def reverslist(s,n):
    
    if len(s) >= n:
        res = ''
        
        for i in range(-1, -n-1, -1):
            
            res +=s[i]
        return res
    
    else:
        raise AssertionError('string length is small')
        
        


def uniqueStr(lstStr):
    
    return len(set(lstStr))



print(uniqueStr(['abc','def', 'abc']))
    
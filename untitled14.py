#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 19:07:50 2021

@author: avinashkumarmishra
"""



def decodeString(numberOfRows, encodedString):
    
    each_row_length = len(encodedString) // numberOfRows
    res = list() 
    i = 0
    for row in range(numberOfRows):
        res.append(encodedString[i:(i+each_row_length)])
        i = i+each_row_length
    
    return type(encodedString)

                
    
print(decodeString(3, 'mnes___ya____mi'))
    
    
    
    
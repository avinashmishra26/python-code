#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 00:28:33 2021

@author: avinashkumarmishra
"""



class Abc:
    
    var = 0
    
    def __init__(self, a):
        self.a = a
        Abc.var += 1
        
    def __hash__(self):
        return self.a + Abc.var
    
    def __eq__(self, other):
        return self.a == other.a and False
    
    def __str__(self):
        return 'A = '+str(self.a)
        
        
        
a1 = Abc(5)

a2 = Abc(5)


a = {a1:1, a2:2}

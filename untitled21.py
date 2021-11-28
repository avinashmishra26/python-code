#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 10:40:21 2021

@author: avinashkumarmishra
"""

class Car(object):
    
    def __init__(self, m, r):
        self.m = m
        self.r = r
        
    def __lt__(self, other):
        return self.r < other.r
        
    def __str__(self):
        return self.m + '0 to 100 Km per hour in'+ self.r
            
            
            
class CarEngine(Car):
    
    def __init__(self, m, r, eType):
        Car.__init__(self, m, r)
        self.eType = eType
        
        
        
    def __str__(self):
        return self.m + '0 to 100 Km per hour in '+ str(self.r)+' Engine Type is ' + str(self.eType)
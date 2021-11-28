# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 20:48:23 2021

@author: avimishr2
"""

class Flight(object):

    """

    data attributes : start, end (strings), duration (float)

    """

    def __init__(self, start, end, duration):
        self.start = start
        self.end = end
        self.duration = duration
        
    def __add__(self, other):
        return (self.duration+other.duration)
    
    
    
f1 = Flight("LHR","FRA",1.5)

f2 = Flight("LHR", "DUB",1.0)

print( f1 + f2)
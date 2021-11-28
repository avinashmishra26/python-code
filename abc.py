# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 20:31:17 2021

@author: avimishr2
"""

def transform (d):
    result = list()
    if isinstance(d, dict):
        for k in d:
            ele = (k, d[k])
            result.append(ele)
    return (result)
        
print(transform({'flamingo':'pink','polar bear':'white'}))



class Rectangle(object):

    """

    data attributes : width, height (both float)

    """

    def __init__(self,width, height):
        self.width = width
        self.height = height\
            
    def perimeter(self):
        return (2*(self.width+self.height))
    
    
    
r = Rectangle(1.0,2.0)
print(r.perimeter())







    
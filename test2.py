# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 20:51:34 2021

@author: avimishr2
"""

def intersects(t1,t2):
    result_tuple = ()
    if isinstance(t1, tuple) and isinstance(t1, tuple):
        for val1 in t1:
            if val1 in t2:
                result_tuple = result_tuple + (val1,)
    return(result_tuple)
    
    
print(intersects(('a','b','c','d'), ('b','k','d')))


myD = {'a' : (2,),'b' : (-5,2),'c' : (5,4,3,1),'d' : (1,1,2)}

def search(myD):
    str_res = str()
    for key in myD:
        if (len(myD[key]) % 2) == 0:
            str_res = str_res + key
    return str_res
    
print(search({'a' : (2,),'b' : (-5,2),'c' : (5,4,3,1),'d' : (1,1,2)}))
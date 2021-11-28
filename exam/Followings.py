#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 11:39:44 2021

@author: avinashkumarmishra
"""

class Followings:
    
    def __init__(self, lst):
        self.follows = {}
        for a, b in lst:
            res = self.follows.get(a,[])
            res.append(b)
            self.follows[a] = res
           
    def followed_by(self, usr_nm):
        return self.follows[usr_nm]
    
    
    def followers_of(self, usr_nm):
        res = []
        for k, v in self.follows.items():
            if usr_nm in v:
                res.append(k)    
        return res
    
    
    def same_out_degree(self):
        res = {}
        for k, v in self.follows.items():
            v1 = len(v)
            temp = res.get(v1, [])
            temp.append(k)
            res[v1] = temp    
        return res       
        
            
f=Followings([('bob','meg'),('bob','kim'),('meg','bob'),('kim','bob'),('kim','tom'),('tom','bob')])    

        
    
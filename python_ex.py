#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 11:23:59 2021

@author: avinashkumarmishra
"""

class Triplets(object):
    
    def __init__(self, triplets_relations):
        self.triplets_relations = triplets_relations
        
        
    def serachTriplets(self, single_relation):
        if single_relation in self.triplets_relations:
            return True
        return False

    def getSubjectObject(self, predicate):
        res = {}
        for sub,pred,obj in self.triplets_relations:
            if pred == predicate:
                obj_lst = res.get(sub,[])
                obj_lst.append(obj)
                res[sub] = obj_lst
                
        return res
        
    
t = Triplets([ ('Shakespeare','wrote','Macbeth'), ('Rowling','wrote','Harry Potter'),\
('Macbeth','is set in','Scotland'),('Harry Potter','is set in','Scotland'),('Harry Potter','is set in','London')])

    
print(t.getSubjectObject('is set in'))
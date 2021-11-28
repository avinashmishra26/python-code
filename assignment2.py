# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 19:37:42 2021

@author: avimishr2
"""

def buildDict(k,v):
    convertToDict = {}
    if(len(k) == len(v)):
        for idx in range(len(k)):
            if k[idx] not in convertToDict:
                convertToDict[k[idx]] = v[idx]
    return convertToDict
    
k = ['milk', 'bread', 'cheese', 'milk']
v = [100, 20, 30, 10]            
print(buildDict(k, v))

##################################################
import math

class Circle(object):
    def __init__(self, radius):
        self.radius=radius
        self.pi = math.pi
            
    def circumference(self):
        return 2*self.pi*self.radius
    
c = Circle(2.0)

print(abs(c.circumference() - 12.566) < 0.001)

############################################################

class Flight(object):
    
    def __init__(self,start,end,duration):
        self.start = start
        self.end = end
        self.duration = duration
        
    def __str__(self):
        return ("{} to {} takes {} hours".format(self.start,self.end,self.duration))
    
c = Flight("LHR","FRA", 1.5)
print(c)  




############################################################


def reversal(l):
    ans = list()
    for i in l:
        if len(i) == 2:
            ele = (i[1],i[0])
        ans.append(ele)
    return ans

print(reversal([(1,2),('a','b'),(3,4)]))
    
    
    
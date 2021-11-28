#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 10:52:06 2021

@author: avinashkumarmishra
"""

class StockQuotes:
    
    
    def __init__(self, stock_quote_lst):      
        self.stock_quote_lst = tuple(sorted(stock_quote_lst, key=lambda x: x[0]))
        
        
    def __str__(self):
        res = ''
        for e in self.stock_quote_lst:
            res += str(e)+'\n'
        return res
        
    def getRMS(self):
        N = 0
        total_val = 0.0
        for _,val in self.stock_quote_lst:
            total_val += val**2
            N +=1
            
        return (total_val/N)**0.5
            
    def lookup(self, s):
        for stock_nm,stock_val in self.stock_quote_lst:
            if stock_nm == s:
                return stock_val
        
    
    
s = StockQuotes([('IBM',35.9),('AZN',159.03)])
print(s.lookup('IBM1'))
        

dit = {"IBM": [11,2,3],"AZN":[10,20,30]}

print(sorted(dit.items(), key=lambda x: x[1][0]))
        

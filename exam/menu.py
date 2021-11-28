#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 19:08:39 2021

@author: avinashkumarmishra
"""

class Menu(object):
    
    def __init__(self,lst):
        self.item = lst
        self.price = {}
        for menu, price in lst:
            self.price[menu] = price

    
    def cost_order(self, orders):
        cost = 0.0
        for ord_key,ord_val  in  orders:
            cost += (self.price[ord_key] * ord_val)
        return cost
    
    def __str__(self):
        res = ""
        for key,val  in  self.price.items():
            res = res + str((key,val)) + '\n'
        return res       



#orders = [('Risotto',1),('Pizza',2)]               
#x = Menu([('Pizza',9.5),('Lasagna', 10.3),('Risotto',8.2)])

#print(x)  

#print(x.cost_order(orders))







class Lunch(Menu):
    
    def __init__(self, lst_of_items):
        
        self.__myvar__ = 1.2
        self.types = {}
        lst = []
        for menu, price, m_type in lst_of_items:
            self.types[menu] = m_type
            lst.append((menu,price))
        Menu.__init__(self,lst)
             
    
    def __str__(self):
        res = ""
        for key,val  in  self.price.items():
            types = self.types[key]
            res = res + str((key,val,types)) + '\n'
        return res
           
             
x = Lunch([('Pizza',9.5, 'Dinner'),('Lasagna', 10.3,'Lunch'),('Risotto',8.2,'Dinner')])
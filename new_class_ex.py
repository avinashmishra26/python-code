# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 16:38:56 2021

@author: avinash
"""

class Fraction(object):
    
    def __init__( self, numerator, denominator):
        if isinstance(numerator, int) and isinstance(denominator, int):
            self.numerator = numerator
            if denominator == 0 :
                self.numerator= 0
                self.denominator= 1
            elif  denominator < 0:
                 self.numerator = numerator*-1
                 self.denominator = denominator*-1
            else:
                self.denominator = denominator
        else:
             self.numerator= 0
             self.denominator= 1
    def __str__(self):
        return ("\""+str(self.numerator)+"/"+str(self.denominator)+"\"")
    
    def __float__(self):
        return self.numerator/self.denominator
    
    def inverse(self):
        if self.numerator == 0:
            return ("0/1")
        elif self.numerator < 0:
            return (str(self.denominator*-1)+"/"+str(self.numerator*-1))
        else:
            return (str(self.denominator)+"/"+str(self.numerator))
        
    def __add__(self, other):
        res_num = self.numerator*other.denominator + other.numerator*self.denominator
        res_deno = self.denominator*other.denominator
        return (str(res_num)+"/"+str(res_deno))
    
    def __sub__(self, other):
        res_num = self.numerator*other.denominator - other.numerator*self.denominator
        res_deno = self.denominator*other.denominator
        return (str(res_num)+"/"+str(res_deno))
        
    
f= Fraction(-1,2)

f1= Fraction(4,5)

print(f -f1)
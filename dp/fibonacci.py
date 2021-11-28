#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 07:36:58 2021

@author: avinash
"""


fib_series = {}

def fibonacci(n):
    if fib_series.get(n, -1) != -1:
        return fib_series[n]
    if n <= 1:
        fib_series[n]=n
        return n
    else:
        firstTerm = fibonacci(n-1)
        secondTerm = fibonacci(n-2)
        fib_series[n-1]=firstTerm
        fib_series[n-2]=secondTerm
        return firstTerm + secondTerm
     
print(fibonacci(7))
        
def fibonacci_best(n):
    if n <= 1:
        return n
    
    f_minus_2, f_minus_1 = 0,1 
    for _ in range(1, n):
        f = f_minus_1 + f_minus_2
        f_minus_2, f_minus_1 = f_minus_1, f
    return f
    
    
    
print(fibonacci_best(7))
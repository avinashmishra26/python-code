#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 13:36:17 2021

@author: avinashkumarmishra
"""

count = 0
with open('demo.txt', 'r') as f:
    for line in f:
        for word in line.split():
            if word.strip('.,').casefold() == 'python':
                count += 1

print(count)



with open('animal.txt', 'a') as f:
    f.write('cat\n')
    
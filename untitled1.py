# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 19:29:39 2021

@author: avina
"""


n = int(input())
i = 0

while i <= n:
    if (4*(i**3) + 3) > n:
        break
    i += 1
        
print(i)        



print("**** 10")
l = input()
s = input()
p = False

rev_str = l[::-1]
print(rev_str)

index = 0
if s.find(rev_str) != -1:
    p = True

print(p)

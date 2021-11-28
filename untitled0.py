#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 15:47:32 2021

@author: avinashkumarmishra
"""

from functools import reduce

a = lambda num: reduce(lambda x,y: x+y, [1.0/(i+1) for i in range(num)])


t = lambda x: True if isinstance(x**(1/3), int) and x**(1.0/3) % 2 == 0 else False



import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return True if re.compile(p).fullmatch(s) else False
        
        
        


s = Solution()
print(s.isMatch("aab",'c*a*b'))

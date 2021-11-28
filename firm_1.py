#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 15:43:03 2021

@author: avinashkumarmishra
"""

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fillMissingBrackets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def fillMissingBrackets(s):
    # Write your code here
    def fillMissingBrackets_tester(s):
        look_up, remain_chars = { '(':')', ')':'(', '{': '}','}': '{', '[': ']', ']': '[' }, []
        for i in range(len(s)):
            if s[i] in look_up:
                val = look_up[s[i]]
                if s[i] in remain_chars:
                   del remain_chars[remain_chars.index(s[i])]
                else:
                    remain_chars.append(val)
            elif s[i] == '?':
                remain_chars.append(s[i])
        
                   
        if not remain_chars:
            return True
        else:
            not_balance, q_char = 0, 0
            for re in remain_chars:
                if re in look_up:
                    not_balance += 1
                elif re == '?':
                    q_char += 1
            if not_balance == q_char:
                return True
                
        return False
        
    return fillMissingBrackets_tester(s)
    #count = 0
    #for idx in range(1, len(s)):
    #    if fillMissingBrackets_tester(s[:idx]) and fillMissingBrackets_tester(s[idx:]):
    #        count += 1
    #return count

print(fillMissingBrackets('(?]['))
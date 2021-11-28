#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 00:50:17 2021

@author: avinashkumarmishra
"""

import math
 

class Solution:
    def arrayNesting(self, nums) -> int:
        highest_cnt = -math.inf
        nums_len = len(nums)
        nums_visited = set()
        for i in range(len(nums)):
            if i in nums_visited:
                continue
            temp_s = {}
            x = i
            while True:
                no = nums[x]
                temp_s[x] = no
                if no in temp_s:
                    break
                x = no
            
            nums_visited.update(temp_s.keys())
            print(temp_s.items())
            break
            
            if highest_cnt < len(temp_s):
                highest_cnt = len(temp_s)
        return highest_cnt
    
s = Solution()
s.arrayNesting([5,4,0,3,1,6,2])
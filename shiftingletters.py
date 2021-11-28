#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 01:10:12 2021

@author: avinashkumarmishra
"""

class ShiftingLetters:
    
    def shiftingLetters(self, s: str, shifts) -> str:
        res = '';
        total = sum(shifts[0:])
        for idx in range(len(s)):
            if idx != 0:
                total -= shifts[idx-1]
            uni_val = (ord(s[idx])%97 + total)%26
            res += chr(uni_val+97)
            
            
        return res 
    
    def shiftingLetters1(self, s: str, shifts) -> str:
        res = '';
        for idx in range(len(s)):
            uni_val = (ord(s[idx]) + sum(shifts[idx:]) %26 )
            if uni_val >= (97 + 26):
                uni_val -= 26       
            res += chr(uni_val)
            
            
        return res    
            
            
    



s = Solution()
print(s.shiftingLetters('ruu', [26,9,17]))
print(s.shiftingLetters1('ruu', [26,9,17]))
        
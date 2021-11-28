#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 23:38:18 2021

@author: avinashkumarmishra
"""


class Solution:
    
    def sum1(self, a, b):
        s = int(a)+int(b)
        
        return str(s)
    
    def sub(self, a, b):
        s =  int(a)-int(b)
        return str(s)
    
    def calculate(self, s: str) -> int:
        stack = []
        stack.append('(')
        
        close_bracket_look_up = {')':'('}
        
        operand_look_up = {'+': self.sum1, '-': self.sub}
        
        s += ')'
        
        for ch in s:
            if ch == ' ':
                continue
            elif ch in close_bracket_look_up.keys():
                prev = stack.pop()
                if prev.isdigit() :
                    while True:
                        new_ch = stack.pop()
                        if new_ch in close_bracket_look_up.values():
                            stack.append(prev)
                            break
                        elif new_ch in operand_look_up:
                            operator = operand_look_up.get(new_ch)
                        elif new_ch.isdigit():
                            prev = operator(new_ch, prev)
                            
                
                else:
                    stack.append(prev)
                    stack.append(ch)
                    
            else: 
                stack.append(ch)
                    
        return stack.pop()
                    
            
        
        
        
        
        
s = Solution()
print(s.calculate("2-1+2"))
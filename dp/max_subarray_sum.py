#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 09:37:37 2021

@author: avinash

 Kadane’s Algorithm:


"""



""" Brute Force Technique"""
import math

def maxSubArraySum(arr):
    max = -math.inf
    count_iter=0
    for i in range(0,len(arr)):
        for j in range(i,len(arr)):
            sum = 0
            for k in range(i,j+1):
                sum+=arr[k]
                count_iter +=1
            if sum > max:
                max = sum
    print('count',count_iter)
    return max


print(maxSubArraySum([904,40, 523, 12, -335, -385, -124, 481, -31]))

print(maxSubArraySum([-2,-3, 4, -1, -2, 1, 5, -3]))
                

print(maxSubArraySum([8,-3, -2]))
            
    
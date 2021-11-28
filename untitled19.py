#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 09:42:15 2021

@author: avinashkumarmishra
"""


def question_1d():
    s_list = list()
    s = input('Enter number :: ')
    
    has_duplicate = False
    
    while s != '':
        s_list.append(s)
        s = input('Enter number :: ')
        if s in s_list:
            has_duplicate = True
        
    s_list.sort()
    
    print(s_list)
    
    if(has_duplicate):
        print('There are duplicates')
    


def question_1c():
     all_num = []
     try :
         n = int(input('Enter number :: '))
        
         while n >= 0:
            all_num.append(n)
            n = int(input('Enter number :: '))
            
        
         for i in range(-1,-len(all_num)-1,-1):
            print(all_num[i])
     except:
        print('Input is not integer')


def question_1b():
    all_num = []
    n = int(input('Enter number :: '))
    
    while n != 0:
        all_num.append(n)
        n = int(input('Enter number :: '))
        
        
    print('All numbers' , all_num)
    print('Their Sum' , sum(all_num))
    print('Their Mean' , sum(all_num)/len(all_num))



def number_div_by_seven(number = 1000):
    for num in range(1, number):
        if num%7 == 0:
            print(num)
            
            
            
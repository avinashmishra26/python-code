# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 19:18:28 2021

@author: avina
"""

n = input('Enter the String ')

str_len = len(n)

if str_len == 0:
    print('String is empty')

#14
for ch in n :
    if ch in 'aeiou':
        print("All vowels are there!")
        break
        
if n[0] == 'a' and n[-1]== 'z':
    print('And it could be alphabetical!')
    
    
#17
def countOccurrences(string, substring):
    
    start = 0
    pos = -1
    count = 0;
    
    while start < len(string):
        pos = string.find(substring, start)
        if pos != -1:
            start = pos + 1
            count +=1
        else :
            break
    return count

print(countOccurrences('iliketartartandmoretart','tart'))
        


    

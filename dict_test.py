# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 18:44:06 2021

@author: avina
"""

groceries = {'milk':1, 'eggs':12, 'bread':2,'cheese':5,'jam':2}
print(groceries)

print(groceries['bread'])

#print(groceries['cucumber'])

print(groceries.keys())

groceries['chicken'] = 4
print(groceries)
groceries['chicken'] = 6
print(groceries)

print('milk' in groceries)

del(groceries['cheese'])
print(groceries)

print('*****'*5)

for key in groceries:
    print(key, groceries[key])
    
    
for key in groceries.keys():
    print(key)
    
for val in groceries.values():
    print(val)
    

L = ['bread']
#for k in groceries:
 #   if k in L:
  #      del(groceries[k])
        
for k in list(groceries):
    if k in L:
        del(groceries[k])
        
print(groceries)
        
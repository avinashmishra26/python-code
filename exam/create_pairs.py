#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 20:41:54 2021

@author: avinashkumarmishra
"""

def createPairs () :
       letters = 'abcdefghijklmnopqrstuvwxyz'
       letList = list ( letters )
       pairs = []
       for i1 in range ( len ( letList ) ) :
              for i2 in range ( i1 , len ( letList ) ) :
                 pairs . append ( letList [ i1 ]+ letList [ i2 ])
       return ( pairs )

# 'aa', 'bb'
"""
Get occurrence of every pair of letters in list of strings
"""
def occurrence ( l ) :
       counts = {}  #1
       pairs = createPairs ()
       for s in l :
          for p in pairs :
             old_value = counts.get(p,0) 
             counts [p] =  old_value + s.count(p) #2-3
       return ( counts )



def highestFrequency ( counts ) :
       N = 0
       hiF = [ ' ' ,0.0]
       for n in counts.values () :
           N += n
       for (p , n ) in counts.items() :     #3
           f = n/N                          #4 
           if f > hiF [1]:
             hiF = [p , f ]
       return ( hiF )




if __name__ == '__main__':   #5
    s = " "
    l = []
   
    while s != 'quit':
        s = input ()   #6
        l . append ( s )
    n = occurrence ( l )
    f = highestFrequency ( n )
    print ( ' Highest frequency pair is '+ f [0]+ ' at '+ str ( f [1]) )
    
    
    

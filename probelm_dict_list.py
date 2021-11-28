# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 19:44:19 2021

@author: avinash
"""

a = input("df")

def lyrics_to_frequencies(lyrics):
    myDict = {}
    for v in range(len(lyrics)):
        if lyrics[v] in myDict:
            myDict[lyrics[v]] +=1
        else:
             myDict[lyrics[v]] = 1
    return myDict


a = "abchcuua"
print(lyrics_to_frequencies(a))


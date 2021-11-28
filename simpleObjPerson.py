#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 15:47:26 2021

@author: avinashkumarmishra
"""

import datetime

class Person(object):
    
    def __init__(self, name):
        self.name = name
        try:
            lastBlank = name.rindex(' ')
            self.lastName = name[lastBlank+1:]
        except:
            self.lastName = name
        self.birthday = None
        
    def getName(self):
        return self.name

    def getLastName(self):
        return self.lastName
    
    def getBirthday(self):
        return self.birthday

    def setBirthday(self, birthday):
        self.birthday = birthday
        
    def getAge(self):
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
    
    def __lt__(self, other):
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
        
    def __str__(self):
        return self.name
    
    
me = Person('Michael Guttag')
him = Person('Barack Hussein Obama')
her = Person('Madona')

print(him.getLastName(), him.lastName)    

him.setBirthday(datetime.date(1961, 8, 4))
her.setBirthday(datetime.date(1958, 8, 16))

print(him.getBirthday(), him.getAge())

lst = [me, him, her]

print('\nNormal Print\n')
for p in lst:
    print(p)
    
print('\nSort Print\n')
lst.sort()
for p in lst:
    print(p)

    
    

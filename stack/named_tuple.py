#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 02:43:14 2021

@author: avinashkumarmishra
"""



from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'DOB'])


s = Student('Avinash', 31, '26-May')

print(s[0], s.age)


print (getattr(s,'DOB'))


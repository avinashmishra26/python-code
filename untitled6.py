#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 15:49:12 2021

@author: avinashkumarmishra
"""
import re
a = list()

def searchSuggestions(repository, customerQuery):
    if len(customerQuery) >=2:
        i = 2
        f_res = []
        while i <= len(customerQuery):
            cus_qry = customerQuery[:i]
            result = list()
            for each_phrase in repository:
                if re.match(r'['+cus_qry+']', each_phrase):
                    result.append(each_phrase)
            result.sort()
            f_res.append(result)
            i += 1
    return f_res
  

print([' '.join(x) for x in \
      searchSuggestions(['bags','baggage', 'banner','box','cloths'] \
                                  ,'bags')])
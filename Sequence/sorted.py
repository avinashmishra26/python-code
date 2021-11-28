# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 18:36:36 2021

@author: avina
"""

empty_list = []
even = [2,4,6,8]
odd = [1,3,5,7]

numbers = even + odd


sorted_number = sorted(numbers)
print(sorted_number)
print(numbers)


numbers.sort()
print(numbers)

digits = sorted("728292098")
print(digits)

str_n = "728292098"
#str_n.sort()        # Error
print(str_n)


d = list("728292098")
print(d)


num1 = [10,20,30]
num2 = [10,20,30]

num3 = [30,20,10]

#check if both are same object
print(num1 is num2)

#content checking
print(num1 == num2)
print(num1 == num3)

#copy number
more_number = numbers[:]
print(more_number)

mre_numbers = numbers.copy()
print(mre_numbers)
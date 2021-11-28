# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 14:57:08 2021

@author: avina
"""


class Coordinate(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def distance(self, other):
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5
    
    def __str__(self):
        return( "<"+str(self.x)+","+str(self.y)+">")
    
    
        
        
c = Coordinate(3,4)
origin = Coordinate(0,0)

print(c.distance(origin))

print(Coordinate.distance(c,origin))

print(c)



print("isinstance:: "+str(isinstance(c,Coordinate)))


print("isinstance:: "+str(isinstance(c,float)))



class Student(object):
    def __init__(self,firstName, surname, ID, age):
        self.firstName = firstName
        self.surname = surname
        self.ID = ID
        self.age = age
        
    def __eq__(self,other):
        if self.age == other.age:
            return True
        else:
            return False
  
    def getFirstName(self):
        return self.firstName
    
    def getSurname(self):
        return self.surname
    
    def getID(self):
         return self.ID
    
    def getAge(self):
         return self.age
    
    def setFirstName(self,firstName):
         self.firstName = firstName
    
    def setSurname(self, surname):
         self.surname =surname
    
    def setID(self, ID):
         self.ID = ID
    
    def setAge(self, age):
         self.age = age


s = Student("Pooh","Bear",1,10)
t = Student("Christopher","Robin",2,10)

print(s == t )
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 21:51:22 2021

@author: avina
"""

class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    def getAge(self):
        return self.age
    def getName(self):
        return self.name
    def setAge(self, newage):
        self.age = newage
    def setName(self, newname=""):
        self.name = newname
        
class Cat(Animal):
    def speak(self):
        print("meow")
    def __str__(self):
        return("cat:"+str(self.name)+":"+str(self.age))

class Rabbit(Animal):
    tag =1  #Java Static Type
    
    def __init__(self,age,parent1=None,parent2=None):
        Animal.__init__(self,age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1
        
    def getRid(self):
        return str(self.rid).zfill(3)
    
    def getParent1(self):
        return self.parent1
    
    def getParent2(self):
        return self.parent2
    
    def  __add__(self,other):
        return (Rabbit(0,self,other))
    
    def __eq__(self, other):
        parentSame = self.parent1.rid == other.parent1.rid \
            and self.parent2.rid == other.parent2.rid
            
        parentOpposite = self.parent1.rid == other.parent2.rid \
            and self.parent2.rid == other.parent1.rid
            
        return (parentSame or parentOpposite)
    
    
    
r1 = Rabbit(4)
r2 = Rabbit(2)
r4 = r1+r2
print(r4.getAge())

print(r4.getParent1().getAge())


r5 = r2+r1

print(r4 == r5)
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 20:32:37 2021

@author: avinash
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



class Person(Animal):
    def __init__(self,name, age):
        Animal.__init__(self, age)
        self.setName(name)
        self.friends = []
    
    def get_friends(self):
        return self.friends
    
    def speak(self):
        print('hello')
    
    def add_friend(self,fname):
        if fname not in self.friends:
            self.friends.append(fname)
    
    def age_diff(self, other):
        diff = self.getAge() - other.getAge()
        print(abs(diff),"year difference")
    
    def __str__(self):
        return ("person:"+str(self.name)+":"+str(self.age))
    
    
class Student(Person):
    def __init__(self, name, age, degree=None):
        Person.__init__(self, name, age)
        self.degree = degree
    def change_degree(self, degree):
        self.degree = degree
    def speak(self):
        r = random.random()
        if r < 0.25:
            print("I have homework")
        elif 0.25 <= r < 0.5:
            print("I need sleep")
        elif 0.5 <= r < 0.75:
            print("I should eat")
        else:
            print("I am watching tv")
 
    def __str__(self):
        return("student:"+str(self.name)+":"+str(self.age)+":"+str(self.degree))
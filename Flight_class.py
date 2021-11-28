# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 23:07:46 2021

@author: avina
"""

class Flight(object):

    allFlightNumbers = list()
    
    def __init__(self,flightNumber,departure,arrival):

        self.flightNumber = flightNumber

        self.departure = departure

        self.arrival = arrival
        
        Flight.allFlightNumbers.append(self.flightNumber)
        
    def showAllFlightNumbers(self):
        print(Flight.allFlightNumbers)
        
        
f1 = Flight("FR243","LTN","KIR")
f2 = Flight("FR244","KIR","LTN")
f3 = Flight("VA3","LHR","JFK")
print(f3.showAllFlightNumbers())
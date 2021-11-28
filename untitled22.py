#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Polygon(object):
    
    def __init__(self, coordinates):
        self.coordinates = list()
        for point in coordinates:
            print(point)
            self.coordinates.append(point)


    def checkPoint(self, point):
        print(point)
        if point in self.coordinates:
            return True
        return False
    
    
    def isConvex(self):
   
        prev, curr = 0, 0
        arr_len = len(self.coordinates)
     
        for i in range(arr_len):
             
            three_point = [self.coordinates[i], self.coordinates[(i + 1) % arr_len], \
                               self.coordinates[(i + 2) % arr_len]]
     
            curr = self.CrossProduct(three_point)
            print(curr)
            if (curr != 0):   
                if (curr * prev < 0):
                    return False
                else:
                    prev = curr
     
        return True
    
    def CrossProduct(self, A):
     
        X1 = (A[1][0] - A[0][0])
        Y1 = (A[1][1] - A[0][1])
        X2 = (A[2][0] - A[0][0])
        Y2 = (A[2][1] - A[0][1])
     
        return (X1 * Y2 - Y1 * X2)
        
    
    
    
p = Polygon([(0,0),(0,1),(1,1),(0.5,0.5),(1,0)])

p.coordinates
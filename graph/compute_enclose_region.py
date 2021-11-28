#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 11:59:27 2021

@author: avinashkumarmishra
"""

import collections

def fill_surrounded_regions (board) :
    row, col = len(board) , len(board[0])
    
    q = collections.deque([ \
        ele for k in range(row) for ele in ((k,0), (k,col-1)) ] + [\
        ele for k in range(col) for ele in ((0,k), (row-1,k))])
                                                                   
    while q:
        x, y = q.popleft()
        
        if 0 <= x < row and 0 <= y < col and board[x][y] == 'W':
            board[x][y] = 'B'
            for x1, y1 in [(1,0),(-1,0),(0,1),(0,-1)]:
                q.append((x+x1,y+y1))
                
    
    
#4X4 matrix
maze = [['B','B','B','B'],['W','B','W','B'],['B','W','W','B'],['B','B','B','B']] 
fill_surrounded_regions(maze)                                                              
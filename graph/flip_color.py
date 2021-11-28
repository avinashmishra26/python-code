#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 19:16:55 2021

@author: avinashkumarmishra
"""

#DFS
import collections

coordinate = collections.namedtuple('coordinate',('x','y'))

def flip_coin_dfs(maze, cur):
    color = maze[cur.x][cur.y]
    
    if color == 'W':
        maze[cur.x][cur.y] = 'B'
    else:
        maze[cur.x][cur.y] = 'W'
    
    
    for d in [(-1,0),(1,0),(0,-1),(0,1)]:
        x_next , y_next = cur.x+d[0] , cur.y+d[1]
        
        if 0<= x_next < len(maze) and 0 <= y_next < len(maze[x_next]) and \
            maze[x_next][y_next] == color:
                flip_coin_dfs(maze, coordinate(x_next,y_next))
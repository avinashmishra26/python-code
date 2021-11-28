#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 16:33:59 2021

@author: avinashkumarmishra
"""

#DFS

import collections

coordinate = collections.namedtuple('coordinate',('x','y'))

def search_maze(maze, s, e):
    
    def search_maze_helper(cur):
        
        if not (0 <= cur.x < len(maze) and 0 <= cur.y < len(maze[cur.x]) and \
           maze[cur.x][cur.y] == 'W'):
               return False
        
        path.append(cur)    
        maze[cur.x][cur.y] = 'B'
        #print(path)
        if cur == e:
            return True
               
               
        if any(map(search_maze_helper,(coordinate(cur.x-1,cur.y), \
                                       coordinate(cur.x+1,cur.y),\
                                       coordinate(cur.x,cur.y-1),\
                                       coordinate(cur.x,cur.y+1)))):
            return True
        else:
            
            del path[-1] 
           
        
    path = []
    
    if not search_maze_helper(s):
        return []
    
    return path 
    

maze = [['W','B','W'],['W','B','W'],['W','W','W']]
print(search_maze(maze, coordinate(2,0),coordinate(0,2)))

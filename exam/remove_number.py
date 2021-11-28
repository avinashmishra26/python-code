#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 14:46:45 2021

@author: avinashkumarmishra
"""

import re

to_str = """
1 from random import random
2
3 class Card (object) :
4 ranks = [ ’2 ’, ’3 ’, ’4 ’ , ’5 ’, ’6 ’, ’7 ’, ’8 ’ , ’9 ’ , ’10 ’ ,
5 ’ Jack ’, ’ Queen ’, ’ King ’ , ’ Ace ’]
6 suits = [ ’ Spades ’ , ’ Clubs ’, ’ Diamonds ’ , ’ Hearts ’]
7
8 def __init__ ( self , rank , suit ):
9 self . rank = rank
10 self . suit = suit
11
12 def __str__ ( self ) :
13 return ’ Card ( ’ + Card . ranks [ rank ] + ’ , ’ + \
14 Card . suits [ suit ] ’) ’
15
16 # Number of players
17 n_players = 5
18
19 # generate a random integer in [0 , n)
20 def get_rand_int (n ):
21 return int( random () ) * n
22
23 def shuffle () :
24 for i in range(len( deck )) :
25 rand_pos = i + get_rand_int (len( deck ) - i)
26 deck [i ] , deck [ rand_pos ] = deck [ rand_pos ], deck [ i]
27
28 # Create a deck of cards
29 for r in range(len( Card . ranks ) ):
30 for s in range(len( Card . suits ) )
31 deck . append ( Card (r , s ))
32
33 # Shuffle the deck
34 deck = shuffle ( deck )
35
36 # Deal 3 cards to each player
37 player_hands = {}
38 for p in range( nPlayers ):
39 player_hands [p ] = ()
40 for j in range (3) :
41 player_hands [p ]. append ( pop ( deck ))
42 # Convert a hand of cards into a string
43 def hand_to_str ( hand ):
44 s = []
45 for c in hand :
46 s . append ( c )
47 return ’ , ’. join ( s )
48
49 # Print the hands
50 for p in player_hands :
51 print( " Player " + p + ’: ’ + hand_to_str ( player_hands [p ])
"""

#to_str = '23def createPairs ()'

def addtoFile(each_line):
    
    each_line = each_line.strip()
    if each_line != "":
    
        with open('abc.py','a') as fp:
            fp.write(each_line)
            fp.write('\n')
        
        

regex = r'^\d+\s'

for each_line in [re.sub(regex, '' ,a1) for a1 in to_str.split('\n')]:
    addtoFile(each_line)





        


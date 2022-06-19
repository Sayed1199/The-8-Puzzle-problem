# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 14:43:06 2022

@author: Sayed
"""

import sys
from copy import deepcopy


class Node:
    
    def setPuzzle(self,puzzle):
        self.curPuzzleState = puzzle 
    
    def printPuzzle(self):
              print(self.curPuzzleState[0][0],self.curPuzzleState[0][1],self.curPuzzleState[0][2])
              print(self.curPuzzleState[1][0],self.curPuzzleState[1][1],self.curPuzzleState[1][2])
              print(self.curPuzzleState[2][0],self.curPuzzleState[2][1],self.curPuzzleState[2][2])
              


class InformedNode:
    
    def __init__(self):
        self.heuristic=0
        self.depth=0
        
    def printPuzzle(self):
        print(self.curPuzzleState[0][0],self.curPuzzleState[0][1],self.curPuzzleState[0][2])
        print(self.curPuzzleState[1][0],self.curPuzzleState[1][1],self.curPuzzleState[1][2])
        print(self.curPuzzleState[2][0],self.curPuzzleState[2][1],self.curPuzzleState[2][2])
        
        
    def setPuzzle(self,puzzle):
        self.curPuzzleState = puzzle     
        
    


def expandPuzzle(puzzle):
    
    expandedList=[]
    
    
    puzzleLeft = deepcopy(puzzle)
    # move blank tile left
    for x in puzzleLeft:
        if(x.count(' ')==1):
            
            if x.index(' ') != 0:
                tileIndex = x.index(' ')
                x[tileIndex] = x[tileIndex - 1]
                x[tileIndex - 1]=' '
                
                expandedList.append(puzzleLeft)
            
    
    puzzleRight = deepcopy(puzzle)
    # move blank tile right
    for x in puzzleRight:
        if(x.count(' ')==1):

            if x.index(' ') != 2:
                tileIndex = x.index(' ')
                x[tileIndex] = x[tileIndex + 1]
                x[tileIndex + 1]=' '
                
                expandedList.append(puzzleRight)
            
    
    puzzleUp = deepcopy(puzzle)
    # move blnak tile Up
    for x in puzzle:
        
        if(x.count(' ')==1):
        
            if( x != puzzleUp[0]):
                tileIndex = x.index(' ')
                
                if ( x == puzzle[1]):
                    puzzleUp[1][tileIndex] = puzzleUp[0][tileIndex]
                    puzzleUp[0][tileIndex] =' '
                    expandedList.append(puzzleUp)
                else:
                    puzzleUp[2][tileIndex] = puzzleUp[1][tileIndex]
                    puzzleUp[1][tileIndex] = ' '
                    expandedList.append(puzzleUp)
            
            
    
    puzzleDown = deepcopy(puzzle)
    # move blnak tile Down
    for x in puzzle:
        if(x.count(' ')==1):

            if( x != puzzleUp[2]):
                tileIndex = x.index(' ')
            
            if ( x == puzzle[0]):
                puzzleDown[0][tileIndex] = puzzleDown[1][tileIndex]
                puzzleDown[1][tileIndex] =' '
                expandedList.append(puzzleDown)
            else:
                puzzleDown[1][tileIndex] = puzzleDown[2][tileIndex]
                puzzleDown[2][tileIndex] = ' '
                expandedList.append(puzzleDown)        
            
    
    return expandedList     




def checkReachedGoal(puzzle,goal):
    return goal == puzzle
        



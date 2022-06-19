# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 15:27:55 2022

@author: Sayed
"""

from puzzleNode import InformedNode,expandPuzzle,checkReachedGoal
import sys

def manhattenDistance(puzzle,goal):
    distance=0
    puzzleContents=['1', '2', '3', '4', '5', '6', '7', '8']
    
    for i in puzzleContents:
        for j in range(3):
            for k in range(3):
                
                if (i ==goal[j][k]):
                    goalRow=j
                    goalCol=k
                    
                if(i==puzzle[j][k]):
                    puzzleRow=j
                    puzzleCol=k
                    
        distance += abs(goalRow-puzzleRow) + abs(goalCol-puzzleCol)
        
    return distance    
           

def bubbleSort(queue):

    for passesLeft in range(len(queue)-1, 0, -1):
        for index in range(passesLeft):
            if (queue[index].heuristic + queue[index].depth) > \
                   (queue[index + 1].heuristic + queue[index + 1].depth):
                queue[index], queue[index + 1] = queue[index + 1], queue[index]

    return queue   


def aStar(puzzle,goal):
    
    nodes_expanded = 0
    max_queue_size = 0
    
    queue=[]
    
    puzzle_node = InformedNode() 
    puzzle_node.setPuzzle(puzzle)
    puzzle_node.depth=0
    puzzle_node.heuristic = manhattenDistance(puzzle_node.curPuzzleState,goal)
    
    queue.append(puzzle_node)
    
    while True:
        if(len(queue)==0):
            print('Search exhausted')
            sys.exit(0)
            
        check_node = InformedNode()
        check_node.curPuzzleState = queue[0].curPuzzleState
        check_node.depth = queue[0].depth
        check_node.heuristic = queue[0].heuristic
        
        check_node.printPuzzle()
        print('expanding this node....')
        
        queue.pop(0)
        
        if(checkReachedGoal(check_node.curPuzzleState, goal)):
            print('found solution bfs: ')
            check_node.printPuzzle()
            print('')
            print('expanded a total of ',nodes_expanded,' nodes')
            print('max number of ndoes in the queue was: ',max_queue_size)
            print('depth is: ',check_node.depth)
            return
        
        print('PuzzleState: ',check_node.curPuzzleState)
        
        expanded_puzzle = expandPuzzle(check_node.curPuzzleState)
        
        for x in expanded_puzzle:
            tempNode = InformedNode()
            tempNode.setPuzzle(x) 
            tempNode.heuristic = manhattenDistance(tempNode.curPuzzleState,goal)
            tempNode.depth = check_node.depth +1
            queue.append(tempNode)
            nodes_expanded+=1
            
            if(len(queue)>max_queue_size):
                max_queue_size = len(queue)
                
        queue= bubbleSort(queue)        
                


























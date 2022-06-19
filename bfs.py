# -*- coding: utf-8 -*-
"""
@author: Sayed
"""

import sys
from puzzleNode import Node,expandPuzzle,checkReachedGoal



def bfs(puzzle,goal):
    
    nodes_expanded = 0
    max_queue_size = 0
    
    queue=[]
    
    puzzle_node = Node()
    puzzle_node.setPuzzle(puzzle)
    
    queue.append(puzzle_node)
    
    while True:
        if(len(queue)==0):
            print('Search exhausted')
            sys.exit(0)
            
        check_node = Node()
        check_node.curPuzzleState = queue[0].curPuzzleState
        
        check_node.printPuzzle()
        print('expanding this node....')
        
        queue.pop(0)
        
        if(checkReachedGoal(check_node.curPuzzleState, goal)):
            print('found solution bfs: ')
            check_node.printPuzzle()
            print('')
            print('expanded a total of ',nodes_expanded,' nodes')
            print('max number of ndoes in the queue was: ',max_queue_size)
            
            return
        
        print('PuzzleState: ',check_node.curPuzzleState)
        
        expanded_puzzle = expandPuzzle(check_node.curPuzzleState)
        
        for x in expanded_puzzle:
            tempNode = Node()
            tempNode.setPuzzle(x)
            queue.append(tempNode)
            nodes_expanded+=1
            
            if(len(queue)>max_queue_size):
                max_queue_size = len(queue)
                
                
        
            
            

    
    

























        


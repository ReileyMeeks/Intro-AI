#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 15:08:27 2021

@author: ReileyMeeks
"""

import queue
import random

class Node:

	def __init__(self, value, par):
	    self.value = value
	    self.parent = par

def readGrid(filename):
	grid = []
	with open(filename) as f:
		for l in f.readlines():
			grid.append([int(x) for x in l.split()])
	
	f.close()
	return grid

def outputGrid(grid, start, goal, path):
	filenameStr = 'path.txt'

	#open file
	f = open(filenameStr, 'w')

	#mark start/goal points
	grid[start[0]][start[1]] = 'S'
	grid[goal[0]][goal[1]] = 'G'

	#mark intermediate points
	for i, p in enumerate(path):
		if i > 0 and i < len(path)-1:
			grid[p[0]][p[1]] = '+'

	#write grid to file
	for r, row in enumerate(grid):
		for c, col in enumerate(row):
			
			if c < len(row)-1:
				f.write(str(col)+' ')
			else:
				f.write(str(col))

		if r < len(grid)-1:
			f.write("\n")

	#close file
	f.close()

#generates a random grid
def genGrid():
    print('In genGrid')
    
    num_rows = 10
    num_cols = 10
    
    grid = [[0]*num_cols for i in range(0,num_rows)]
    
    max_cost = 5
    ob_cost = 0
    
    for i_r in range(0,num_rows):
        for i_c in range(0,num_cols):
            
            # Default to obstacle cost
            cost = ob_cost
            
            # Chance to be an obstacle
            chance = random.random()
            if chance > 0.2:
                # Generate a random cost for the location
                cost = random.randint(1,max_cost)
                
            grid[i_r][i_c] = cost

    return grid

def printGrid(grid):
    for i in range(len(grid)):
        print(grid[i])


def InList(node, theList):
    for n in theList:
        if n.value == node.value:
            return True
    return False

def printNodeList(l):
    for node in l:
        print(node.value)

def getNeighbors(location, grid):
    result = []

    up = location[:]
    up[0] -= 1
    if up[0] > -1 and grid[up[0]][up[1]] != 0:
        result.append(up)

    right = location[:]
    right[1] += 1
    if right[1] < len(grid[right[0]]) and grid[right[0]][right[1]] != 0:
        result.append(right)

    down = location[:]
    down[0] += 1
    if down[0] < len(grid) and grid[down[0]][down[1]] != 0:
        result.append(down)

    left = location[:]
    left[1] -= 1
    if left[1] > -1 and grid[left[0]][left[1]] != 0:
        result.append(left)

    return result

def expandNode(node, openList, openListCopy, closedList, grid):   
    neighbors = getNeighbors(node.value, grid)
    for n in neighbors:
        nd = Node(n, node)

        if not InList(nd, closedList) and not InList(nd, openListCopy):
            openList.put(nd)
            openListCopy.append(nd)

def setPath(current, path):
    while current.parent != '':
        path.insert(0, current.parent.value)
        current = current.parent

def uninformedSearch(type, grid, start, goal):
    print('\nStarting search, type: %s start: %s goal: %s' % (type, start, goal))

    current = Node(start, '')
    path = []

    #determine type of queue to be used
    openList = queue.Queue() if type == 'bfs' else queue.LifoQueue() 

    openListCopy = []

    #push root node onto open list
    openList.put(current)
    openListCopy.append(current)

    #expanded nodes
    closedList = []

    #number of expanded nodes
    numExpanded = 0

    #loop to find goal
    while not openList.empty():
        current = openList.get()
        closedList.append(current)
        
        #check if goal
        if current.value == goal:
            break
        else:
            #expand node
            expandNode(current, openList, openListCopy, closedList, grid)
            numExpanded += 1
 
    #if goal found, build path
    if not openList.empty() or current == goal:
        #set path variable
        setPath(current, path)

        #append goal
        path.append(goal)

    return [path, numExpanded]

def main():
    print('Starting main function for uninformedSearch program')
    grid = readGrid('gridT.txt')
    print ('Grid read from file: %s' % grid)

    #ask user input
    algo = input('Please enter input \"bfs\" or \"dfs\"\n')

#check if valid
    if algo != "bfs" and algo != "dfs":
        print('Invalid input')
    else:
        start = [1,1]
        goal = [6,8]
        [p, numExpanded] = uninformedSearch(algo, grid, start, goal)
        if len(p) > 0:
            print('\nFinal path: %s' % p)
            print('\nNumber of nodes expanded: %d' % numExpanded)
            print('Path cost: %d' % len(p))
            outputGrid(grid, start, goal, p)
            print('\n\nPath written to file path.txt')
        else:
            print('No path could be found')

if __name__ == '__main__':
    main()
    print('\nExiting normally')